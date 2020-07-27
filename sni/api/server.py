"""
API Server
"""

import logging
# from multiprocessing import Process

from fastapi import FastAPI

import uvicorn
import yaml

from sni.conf import CONFIGURATION as conf
from sni.api.routers.alliance import router as router_alliance
from sni.api.routers.callback import router as router_callback
from sni.api.routers.coalition import router as router_coalition
from sni.api.routers.corporation import router as router_corporation
from sni.api.routers.crash import router as router_crash
from sni.api.routers.esi import router as router_esi
from sni.api.routers.group import router as router_group
from sni.api.routers.system import router as router_system
from sni.api.routers.token import router as router_token
from sni.api.routers.user import router as router_user

app = FastAPI()

app.include_router(
    router_alliance,
    prefix='/alliance',
    tags=['Alliance management'],
)

app.include_router(
    router_callback,
    prefix='/callback',
    tags=['Callbacks'],
)

app.include_router(
    router_coalition,
    prefix='/coalition',
    tags=['Coalition management'],
)

app.include_router(
    router_corporation,
    prefix='/corporation',
    tags=['Corporation management'],
)

app.include_router(
    router_crash,
    prefix='/crash',
    tags=['Crash reports'],
)

if conf.discord.enabled:
    from sni.api.routers.discord import router as router_discord
    app.include_router(
        router_discord,
        prefix='/discord',
        tags=['Discord'],
    )

app.include_router(
    router_esi,
    prefix='/esi',
    tags=['ESI'],
)

app.include_router(
    router_group,
    prefix='/group',
    tags=['Group management'],
)

if conf.teamspeak.enabled:
    from sni.api.routers.teamspeak import router as router_teamspeak
    app.include_router(
        router_teamspeak,
        prefix='/teamspeak',
        tags=['Teamspeak'],
    )

app.include_router(
    router_system,
    prefix='/system',
    tags=['System administration'],
)

app.include_router(
    router_token,
    prefix='/token',
    tags=['Authentication & tokens'],
)

app.include_router(
    router_user,
    prefix='/user',
    tags=['User management'],
)


@app.get('/ping', tags=['Testing'], summary='Replies "pong"')
async def get_ping():
    """
    Replies ``pong``. That is all.
    """
    return 'pong'


def print_openapi_spec() -> None:
    """
    Print the OpenAPI specification of the server in YAML.
    """
    print(yaml.dump(app.openapi()))


def start_api_server():
    """
    Starts the API server for real. See
    :meth:`sni.api.server.start_api_server`.
    """
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                '()': 'uvicorn.logging.DefaultFormatter',
                'fmt': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                'use_colors': None,
            },
            'access': {
                '()':
                'uvicorn.logging.AccessFormatter',
                'fmt': ('%(levelprefix)s %(client_addr)s - "%(request_line)s" '
                        '%(status_code)s'),
            },
        },
        'handlers': {
            'default': {
                'formatter': 'default',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stderr',
            },
            'access': {
                'formatter': 'access',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': conf.general.logging_level.upper(),
            },
            'uvicorn.error': {
                'level': conf.general.logging_level.upper(),
            },
            'uvicorn.access': {
                'handlers': ['access'],
                'level': conf.general.logging_level.upper(),
                'propagate': False,
            },
        },
    }
    logging.info(
        'Starting API server on %s:%s',
        conf.general.host,
        conf.general.port,
    )
    try:
        uvicorn.run(
            'sni.api.server:app',
            host=str(conf.general.host),
            log_config=log_config,
            log_level=conf.general.logging_level,
            port=conf.general.port,
        )
    finally:
        logging.info('API server stopped')


# def start_api_server():
#     """
#     Runs the API server in a dedicated process.
#     """
#     Process(
#         daemon=True,
#         name='api_server',
#         target=_start_api_server,
#     ).start()
