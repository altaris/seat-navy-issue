"""
Redis based TTL cache
"""

from typing import Any, Optional
import hashlib
import json
import logging

from redis.exceptions import RedisError

from .redis import new_redis_connection

connection = new_redis_connection()


def cache_get(key: Any) -> Optional[Any]:
    """
    Retrieves a value from the cache, or returns None if the key is unknown.
    The key must be a JSON-dumpable variable.
    """
    hashed_key = hash_key(key)
    result = connection.get(hashed_key)
    if result is not None:
        logging.debug("Cache hit %s %s", hashed_key, str(key)[:20])
        return json.loads(result)
    return None


def cache_set(key: Any, value: Any, ttl: int = 60) -> None:
    """
    Sets a value in the cache. The key and value must be JSON-dumpable.
    """
    try:
        connection.setex(hash_key(key), ttl, json.dumps(value))
    except RedisError as error:
        logging.error("Redis error: %s", str(error))


def hash_key(document: Any) -> str:
    """
    Hashes a JSON-dumpable variable
    """
    return hashlib.md5(  # nosec
        json.dumps(document, sort_keys=True).encode(),
    ).hexdigest()


def invalidate_cache(key: Any):
    """
    Invalidates a cache value
    """
    connection.delete(hash_key(key))