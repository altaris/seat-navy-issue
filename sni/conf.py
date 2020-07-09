"""
Configuration facility
"""

import collections
from typing import Any, Dict, List, MutableMapping, Tuple
import logging
import yaml

CONFIGURATION: Dict[str, Any] = {
    'database.authentication_source': 'admin',
    'database.database': 'sni',
    'database.port': 27017,
    'database.username': 'sni',
    'discord.enabled': False,
    'discord.log_channel_id': None,
    'general.debug': False,
    'general.host': '0.0.0.0',
    'general.logging_level': 'info',
    'general.port': 80,
    'general.scheduler_thread_count': 5,
    'jwt.algorithm': 'HS256',
    'redis.database': 0,
    'redis.port': 6379,
    'teamspeak.auth_group_name': 'SNI TS AUTH',
    'teamspeak.bot_name': 'SeAT Navy Issue',
    'teamspeak.enabled': False,
    'teamspeak.port': 10011,
    'teamspeak.server_id': 0,
    'teamspeak.username': 'sni',
}


def assert_is_set(key: str) -> None:
    """
    Raises an exception if the configuration dict does not have that key.
    """
    if key not in CONFIGURATION:
        raise RuntimeError(f'Configuration key {key} not set')


def load_configuration_file(path: str) -> None:
    """
    Loads the configuration from a YAML file.

    Also sets default values.
    """
    with open(path, 'r') as file:
        file_config = yaml.safe_load(file.read())
    global CONFIGURATION
    CONFIGURATION.update(flatten_dict(file_config))
    CONFIGURATION['logging'] = file_config.get('logging', {})

    assert_is_set('database.authentication_source')
    assert_is_set('database.database')
    assert_is_set('database.host')
    assert_is_set('database.password')
    assert_is_set('database.port')
    assert_is_set('database.username')

    assert_is_set('discord.enabled')
    if get('discord.enabled'):
        assert_is_set('discord.auth_channel_id')
        assert_is_set('discord.log_channel_id')
        assert_is_set('discord.server_id')
        assert_is_set('discord.token')

    assert_is_set('esi.client_id')
    assert_is_set('esi.client_secret')

    assert_is_set('general.debug')
    assert_is_set('general.host')
    assert_is_set('general.logging_level')
    assert_is_set('general.port')
    assert_is_set('general.root_url')
    assert_is_set('general.scheduler_thread_count')

    assert_is_set('jwt.algorithm')
    assert_is_set('jwt.secret')

    assert_is_set('redis.database')
    assert_is_set('redis.host')
    assert_is_set('redis.port')

    assert_is_set('teamspeak.enabled')
    if get('teamspeak.enabled'):
        assert_is_set('teamspeak.auth_group_name')
        assert_is_set('teamspeak.bot_name')
        assert_is_set('teamspeak.enabled')
        assert_is_set('teamspeak.host')
        assert_is_set('teamspeak.password')
        assert_is_set('teamspeak.port')
        assert_is_set('teamspeak.server_id')
        assert_is_set('teamspeak.username')


def flatten_dict(nested_dict: MutableMapping[Any, Any],
                 parent_key: str = '',
                 separator: str = '.') -> dict:
    """
    Flattens a dictionnary.

    `Credits to Imran <https://stackoverflow.com/a/6027615>`_.

    >>> flatten_dict({
        'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}},
        'd': [1, 2, 3],
    })
    {'a': 1, 'c_a': 2, 'c_b_x': 5, 'd': [1, 2, 3], 'c_b_y': 10}

    """
    items: List[Tuple[Any, Any]] = []
    for key, val in nested_dict.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(val, collections.MutableMapping):
            items.extend(flatten_dict(val, new_key, separator).items())
        else:
            items.append((new_key, val))
    return dict(items)


def get(key: str, default: Any = None) -> Any:
    """
    Gets a config value from a key.
    """
    if key in CONFIGURATION:
        return CONFIGURATION[key]
    logging.warning('Unknown configuration key %s', key)
    return default
