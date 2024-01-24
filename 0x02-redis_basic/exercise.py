#!/usr/bin/env python3
"""
Contais a `Cache` class implemented using Redis.
"""
import redis
from functools import wraps
from typing import Any, Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """A decorator that stores number of calls to `method` in Redis
    using the methods `__qualname__` as key, and returns the value
    returned by the original method."""
    @wraps(method)
    def wrapper(self, *args):
        """A wrapper function for the decorator"""
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """A decorator that stores, in Redis, inputs and outputs history of calls
    to `method` using the methods `__qualname__` as key, and returns the value
    returned by the original method."""
    @wraps(method)
    def wrapper(self, *args):
        """A wrapper function for the decorator"""
        key = method.__qualname__
        inputs_key = key + ':inputs'
        outputs_key = key + ':outputs'
        output = method(self, *args)
        self._redis.rpush(inputs_key, str(args))
        self._redis.rpush(outputs_key, str(output))
        return output
    return wrapper


class Cache():
    """Abstracts a cache using Redis."""
    def __init__(self):
        """Instatiates a Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with randomly generated
        string key, and returns the key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[Any], Any]] = None) -> Any:
        """Takes a `key` string and an optional callable `fn`. Gets value
        associated with `key` from Redis and type cast the vaule using `fn`
        before returning it."""
        value = self._redis.get(key)
        if value is None or fn is None:
            return value
        return fn(value)

    def get_str(self, key: str) -> str:
        """Calls `self.get` with string casting function as `fn` parameter."""
        return self.get(key, str)

    def get_int(self, key) -> int:
        """Calls `self.get` with integer casting function as `fn` parameter."""
        return self.get(key, int)
