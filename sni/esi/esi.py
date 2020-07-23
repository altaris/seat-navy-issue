"""
EVE ESI (public API) layer
"""

from typing import Any, Dict, Optional, Tuple
import logging
import re

from dateutil import parser
import mongoengine as me
import pydantic as pdt
from requests import request, Response

import sni.conf as conf
import sni.utils as utils
from sni.db.cache import cache_get, cache_set

from .models import EsiPath

ESI_BASE = 'https://esi.evetech.net/'
ESI_SWAGGER = ESI_BASE + 'latest/swagger.json'


class EsiResponse(pdt.BaseModel):
    """
    A model for ESI responses
    """
    data: Any
    headers: dict = {}
    id_annotations: dict = {}
    status_code: int


ESI_ANNOTATORS: Dict[str, Tuple[str, str]] = {
    'alliance_id': ('latest/alliances/{}/', 'name'),
    'asteroid_belt_id': ('latest/universe/asteroid_belts/{}/', 'name'),
    'category_id': ('latest/universe/categories/{}/', 'name'),
    'character_id': ('latest/characters/{}/', 'name'),
    'constellation_id': ('latest/universe/constellations/{}/', 'name'),
    'corporation_id': ('latest/corporations/{}/', 'name'),
    'graphic_id': ('latest/universe/graphics/{}/', 'graphic_file'),
    'group_id': ('latest/universe/groups/{}/', 'name'),
    'moon_id': ('latest/universe/moons/{}/', 'name'),
    'planet_id': ('latest/universe/planets/{}/', 'name'),
    'region_id': ('latest/universe/regions/{}/', 'name'),
    'star_id': ('latest/universe/stars/{}/', 'name'),
    'stargate_id': ('latest/universe/stargates/{}/', 'name'),
    'station_id': ('latest/universe/stations/{}/', 'name'),
    'system_id': ('latest/universe/systems/{}/', 'name'),
    'type_id': ('latest/universe/types/{}/', 'name'),
}
"""ESI annotators, see :meth:`sni.esi.esi.annotate`"""


def esi_delete(path: str,
               token: Optional[str] = None,
               **kwargs) -> EsiResponse:
    """
    Wrapper for :meth:`sni.esi.esi.esi_request` for DELETE requests.
    """
    return esi_request('delete', path, token, **kwargs)


def esi_get(path: str, token: Optional[str] = None, **kwargs) -> EsiResponse:
    """
    Wrapper for :meth:`sni.esi.esi.esi_request` for GET requests.
    """
    return esi_request('get', path, token, **kwargs)


def esi_get_all_pages(path: str,
                      token: Optional[str] = None,
                      **kwargs) -> EsiResponse:
    """
    Returns all pages of an ESI GET path
    """
    current_page = 1
    max_page = 1
    response_data = []
    response_headers = {}
    response_status_code = -1
    if 'params' not in kwargs:
        kwargs['params'] = {}
    while current_page <= max_page:
        kwargs['params']['page'] = current_page
        current_response = esi_request('get', path, token, **kwargs)
        response_data += current_response.data
        response_headers = current_response.headers
        response_status_code = current_response.status_code
        max_page = int(current_response.headers.get('X-Pages', -1))
        current_page += 1
    return EsiResponse(
        data=response_data,
        headers=response_headers,
        status_code=response_status_code,
    )


def esi_post(path: str, token: Optional[str] = None, **kwargs) -> EsiResponse:
    """
    Wrapper for :meth:`sni.esi.esi.esi_request` for POST requests.
    """
    return esi_request('post', path, token, **kwargs)


def esi_put(path: str, token: Optional[str] = None, **kwargs) -> EsiResponse:
    """
    Wrapper for :meth:`sni.esi.esi.esi_request` for PUT requests.
    """
    return esi_request('put', path, token, **kwargs)


def esi_request(http_method: str,
                path: str,
                token: Optional[str] = None,
                **kwargs) -> EsiResponse:
    """
    Makes an HTTP request to the ESI, and returns the response object.
    """
    kwargs['headers'] = {
        'Accept-Encoding': 'gzip',
        'accept': 'application/json',
        'User-Agent': 'SeAT Navy Issue @ ' + conf.get('general.root_url'),
        **kwargs.get('headers', {})
    }
    if token:
        kwargs['headers']['Authorization'] = 'Bearer ' + token

    if http_method.upper() != 'GET':
        raw = request(http_method, ESI_BASE + path, **kwargs)
        raw.raise_for_status()
        return to_esi_response(raw)

    key = [path, token, kwargs.get('params')]
    response = cache_get(key)
    if response is not None:
        return EsiResponse(**response)

    raw = request(http_method, ESI_BASE + path, **kwargs)
    raw.raise_for_status()
    response = to_esi_response(raw)

    ttl = 60
    if 'Expires' in response.headers:
        ttl = int((parser.parse(response.headers['Expires']) -
                   utils.now()).total_seconds())
    cache_set(key, response.dict(), ttl)

    return response


def get_esi_path_scope(path: str) -> Optional[str]:
    """
    Returns the ESI scope that is required for a given ESI path.

    Raises :class:`mongoengine.DoesNotExist` if no suitable path is found.

    Examples:

        >>> get_esi_path_scope('latest/characters/0000000000/assets')
        'esi-assets.read_assets.v1'

        >>> get_esi_path_scope('latest/alliances')
        None
    """
    esi_path: EsiPath
    for esi_path in EsiPath.objects:
        # print(esi_path.to_json())
        if re.search(esi_path.path_re, path):
            return esi_path.scope
    raise me.DoesNotExist


def id_annotations(data: Any) -> Dict[int, str]:
    """
    Annotates a JSON document. In documents returned by the ESI, ID fields
    always have the same name (e.g. `solar_system_id`, `character_id`, etc.).
    This method recursively searches for these ID fields and returns a dict
    mapping these IDs to a name.
    """
    if isinstance(data, dict):
        annotations = {}
        for key, val in data.items():
            annotator = ESI_ANNOTATORS.get(key)
            if annotator is not None and isinstance(val, int):
                raw = esi_get(annotator[0].format(val))
                annotations[val] = raw.data[annotator[1]]
            else:
                annotations.update(id_annotations(val))
        return annotations
    if isinstance(data, list):
        annotations = {}
        for element in data:
            annotations.update(id_annotations(element))
        return annotations
    return {}


def load_esi_openapi() -> None:
    """
    Loads the ESI Swagger API into the database.

    Should be called in the initialization stage.

    See also:
        :class:`sni.esi.esi.EsiPath`
        `EVE Swagger Interface <https://esi.evetech.net/ui>`_
        `EVE Swagger Interface (JSON) <https://esi.evetech.net/latest/swagger.json>`_
    """
    logging.info('Loading ESI swagger specifications %s', ESI_SWAGGER)
    swagger = request('GET', ESI_SWAGGER).json()
    base_path = swagger['basePath'][1:]
    for path, path_data in swagger['paths'].items():
        for method, method_data in path_data.items():
            full_path = base_path + path
            path_re = '^' + re.sub(r'{\w+_id}', '[^/]+', full_path) + '?$'
            scope = None
            for security in method_data.get('security', []):
                scope = security.get('evesso', [scope])[0]
            EsiPath.objects(
                http_method=method,
                path=full_path,
            ).update(
                set__http_method=method,
                set__path_re=path_re,
                set__path=full_path,
                set__scope=scope,
                set__version='latest',
                upsert=True,
            )


def to_esi_response(response: Response) -> EsiResponse:
    """
    Converts a :class:`request.Response` object to a
    :class:`sni.esi.esi.EsiResponse`.
    """
    return EsiResponse(
        data=response.json(),
        headers=response.headers,
        status_code=response.status_code,
    )
