"""
Teamspeak management.

See also:
    `Teamspeak 3 query server documentation <https://drive.google.com/file/d/1d2y5daxBR7mo92g1IxOKB6A14Ok2-R7T/view?usp=sharing>`_
"""

import logging
from typing import Any, Callable, List, Optional

import pydantic as pdt
from ts3.query import TS3Connection, TS3QueryError

from sni.conf import CONFIGURATION as conf
from sni.db.cache import cache_get, cache_set, invalidate_cache
from sni.user.models import User
from sni.user.user import ensure_autogroup
from sni.utils import HOUR
import sni.utils as utils

from .models import TeamspeakAuthenticationChallenge

TS3_MAX_SIZE_AWAY_MESSAGE = 80
TS3_MAX_SIZE_CLIENT_DESCRIPTION = 200
TS3_MAX_SIZE_CLIENT_NICKNAME_NONSDK = 30
TS3_MAX_SIZE_COMPLAIN_MESSAGE = 200
TS3_MAX_SIZE_GROUP_NAME = 30
TS3_MAX_SIZE_HOST_MESSAGE = 200
TS3_MAX_SIZE_OFFLINE_MESSAGE = 4096
TS3_MAX_SIZE_OFFLINE_MESSAGE_SUBJECT = 200
TS3_MAX_SIZE_POKE_MESSAGE = 100
TS3_MAX_SIZE_TALK_REQUEST_MESSAGE = 50
TS3_MIN_SIZE_CLIENT_NICKNAME_NONSDK = 3


class TeamspeakClient(pdt.BaseModel):
    """
    Represents a teamspeak client as reported by the teamspeak query server.
    """

    cid: int
    clid: int
    client_database_id: int
    client_nickname: str
    client_type: int


class TeamspeakGroup(pdt.BaseModel):
    """
    Represents a teamspeak group as reported by the teamspeak query server.
    """

    iconid: int
    name: str
    savedb: int
    sgid: int
    type: int


def cached_teamspeak_query(
    connection: TS3Connection,
    query: Callable,
    ttl: int = 60,
    *,
    args=list(),
    kwargs=dict(),
) -> Any:
    """
    Returns a parsed query result, and caches the result.
    """
    key = (
        "ts:" + query.__name__,
        [args, sorted(kwargs.items())],
    )
    result = cache_get(key)
    if result is None:
        result = query(connection, *args, **kwargs).parsed
        cache_set(key, result, ttl)
    return result


def client_list(connection: TS3Connection) -> List[TeamspeakClient]:
    """
    Returns the list of clients currently connected to the teamspeak server.

    See also:
        :class:`sni.teamspeak.TeamspeakClient`
    """
    return [
        TeamspeakClient(**raw)
        for raw in TS3Connection.clientlist(connection).parsed
    ]


def close_teamspeak_connection(connection: TS3Connection) -> None:
    """
    Closes a Teamspeak connection. Wraps :meth:`ts3.query.TS3Connection.close`
    in a `try... except` block to catch spurious connection reset exceptions.
    """
    try:
        connection.close()
    except Exception as error:
        logging.warning(
            (
                "Closing Teamspeak connection raised a potentially spurious "
                "exception: (%s) %s"
            ),
            str(type(error)),
            str(error),
        )


def complete_authentication_challenge(connection: TS3Connection, usr: User):
    """
    Complete an authentication challenge, see
    :meth:`sni.teamspeak.new_authentication_challenge`.
    """
    challenge: TeamspeakAuthenticationChallenge = TeamspeakAuthenticationChallenge.objects.get(
        user=usr
    )
    client = find_client(connection, nickname=challenge.challenge_nickname)
    usr.teamspeak_cldbid = client.client_database_id
    usr.save()
    auth_group = ensure_autogroup(conf.teamspeak.auth_group_name)
    auth_group.modify(add_to_set__members=usr)
    challenge.delete()
    logging.info(
        "Completed authentication challenge for %s", usr.character_name
    )


def ensure_group(connection: TS3Connection, name: str) -> TeamspeakGroup:
    """
    Ensures that a teamspeak group exists, and returns a
    :class:`sni.teamspeak.teamspeak.TeamspeakGroup`.
    """
    name = name[:TS3_MAX_SIZE_GROUP_NAME]
    try:
        return find_group(connection, name=name)
    except LookupError:
        invalidate_cache(
            ("ts:" + TS3Connection.servergrouplist.__name__, [[], []])
        )
        connection.servergroupadd(name=name)
        logging.debug("Created Teamspeak group %s", name)
        return find_group(connection, name=name)


def find_client(
    connection: TS3Connection,
    *,
    nickname: Optional[str] = None,
    client_database_id: Optional[int] = None,
) -> TeamspeakClient:
    """
    Returns the :class:`sni.teamspeak.TeamspeakClient` representation of a
    client. Raises a :class:`LookupError` if the client is not found, or if
    multiple client with the same nickname are found.
    """
    clients = [
        client
        for client in client_list(connection)
        if client.client_nickname == nickname
        or client.client_database_id == client_database_id
    ]
    if len(clients) != 1:
        raise LookupError(
            (
                f'Could not find client with nickname "{nickname}" or '
                f"with database id {client_database_id}"
            )
        )
    return clients[0]


def find_group(
    connection: TS3Connection,
    *,
    name: Optional[str] = None,
    group_id: Optional[int] = None,
) -> TeamspeakGroup:
    """
    Returns the :class:`sni.teamspeak.TeamspeakGroup` representation of a
    teamspeak group. Raises a :class:`LookupError` if the group is not found.
    """
    groups = [
        grp
        for grp in group_list(connection)
        if grp.sgid == group_id or grp.name == name
    ]
    if len(groups) != 1:
        display_name = f'"{name}"' if name is not None else "N/A"
        display_group_id = group_id if group_id is not None else "N/A"
        raise LookupError(
            (
                f"Could not find a group with name {display_name} "
                f"or with id {display_group_id}"
            )
        )
    return groups[0]


def group_list(connection: TS3Connection) -> List[TeamspeakGroup]:
    """
    Returns the list of groups in the teamspeak server.

    See also:
        :class:`sni.teamspeak.TeamspeakGroup`
    """
    return [
        TeamspeakGroup(**raw)
        for raw in cached_teamspeak_query(
            connection, TS3Connection.servergrouplist, 1 * HOUR,
        )
    ]


def new_authentication_challenge(usr: User) -> str:
    """
    Initiates an authentication challenge. The challenge proceeds as follows:

    1. A user (:class:`sni.user`) asks to start a challenge by calling
       this method.

    2. This methods returns a UUID, and the user has 60 seconds to change its
       teamspeak nickname to that UUID.

    3. The user notifies SNI that (s)he has done so.

    4. The server checks (see
       :meth:`sni.teamspeak.complete_authentication_challenge`), and if
       sucessful, the corresponding teamspeak client is registered in the
       database and bound to that user. The nickname is also automatically
       assigned.
    """
    logging.info(
        "Starting authentication challenge for %s", usr.character_name
    )
    challenge_nickname = utils.random_code(20)
    TeamspeakAuthenticationChallenge.objects(user=usr).update(
        set__challenge_nickname=challenge_nickname,
        set__created_on=utils.now(),
        set__user=usr,
        upsert=True,
    )
    return challenge_nickname


def new_teamspeak_connection() -> TS3Connection:
    """
    Returns a new connection to the teamspeak server.
    """
    if conf.teamspeak.password is None:
        raise RuntimeError("Configuration key conf.teamspeak.password is None")
    connection = TS3Connection(conf.teamspeak.host, conf.teamspeak.port)
    connection.use(sid=conf.teamspeak.server_id)
    username = conf.teamspeak.username
    connection.login(
        client_login_name=username,
        client_login_password=conf.teamspeak.password.get_secret_value(),
    )
    try:
        connection.clientupdate(client_nickname=conf.teamspeak.bot_name)
    except TS3QueryError:
        pass
    logging.info(
        'Connected to teamspeak server %s:%d as "%s"',
        conf.teamspeak.host,
        conf.teamspeak.port,
        username,
    )
    return connection
