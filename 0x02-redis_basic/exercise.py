#!/usr/bin/env python3
"""
Contais a `Cache` class implemented using Redis.
"""
import redis
from typing import Union
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
