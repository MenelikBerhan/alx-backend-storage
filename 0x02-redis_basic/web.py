#!/usr/bin/env python3
"""
Contais a function that keeps track of url requests.
"""
import redis
import requests
import requests_cache
from functools import wraps
from typing import Callable

cache = redis.Redis()


def count_access(method: Callable) -> Callable:
    """A decorator that tracks how many times a particular URL was accessed
    in the key "count:{url}" and cache the result with an expiration time
    of 10 seconds."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """A wrapper function for the decorator"""
        cache.incr(f'count:{{{url}}}', 1)
        cached_response = cache.get(url)
        if cached_response:
            return cached_response.decode()

        with requests_cache.enabled():
            # Set the cache name and backend
            requests_cache.install_cache(
                cache_name='my_cache',
                backend='redis',
                expire_after=10  # Set expiration time of 10 seconds
            )
        response = method(url)
        cache.set(url, response, ex=10)
        return response
    return wrapper


@count_access
def get_page(url: str) -> str:
    """Obtain the HTML content of `url` and returns it."""
    return requests.get(url).text
