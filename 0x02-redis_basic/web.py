#!/usr/bin/env python3
"""
Contais a function that keeps track of url requests.
"""
import redis
import requests
from functools import wraps
from typing import Callable


def count_access(method: Callable) -> Callable:
    """A decorator that tracks how many times a particular URL was accessed
    in the key "count:{url}" and cache the result with an expiration time
    of 10 seconds."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """A wrapper function for the decorator"""
        cache = redis.Redis()
        cache.incr(f'count:{{{url}}}', 1)
        response = method(url)
        cache.set(url, response, ex=10)
        return cache.get(url)
    return wrapper


@count_access
def get_page(url: str) -> str:
    """Obtain the HTML content of `url` and returns it."""
    return requests.get(url).text
