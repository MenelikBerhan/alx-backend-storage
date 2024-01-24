#!/usr/bin/env python3
"""
Contais a `Cache` class implemented using Redis.
"""
import redis
from typing import Any, Callable, Optional, Union
from uuid import uuid4


class Cache():
    """Abstracts a cache using Redis."""
    def __init__(self):
        """Instatiates a Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with randomly generated
        string key, and returns the key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[Any], Any]]) -> Any:
        """Takes a `key` string and an optional callable `fn`. Gets value
        associated with `key` from Redis and type cast the vaule using `fn`
        before returning it."""
        value = self._redis.get(key)
        if value is None or fn is None:
            return value
        return fn(value)

    def get_str(self, value):
        """Casts value to a string"""
        pass

    def get_int(self, value):
        """Casts value to an integer"""
        pass
