#!/usr/bin/env python3
"""
Contais a function that keeps track of url requests.
"""
import redis
import requests
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
        cache = redis.Redis()
        cache.incr(f'count:{url}', 1)
        cached_response = cache.get(url)
        if cached_response:
            return cached_response.decode()

        try:
            response = method(url)
            if response.status_code == 200:
                cache.set(url, response.text, ex=10)
                return response.text
            else:
                # Handle non-200 response
                return f"Error: {response.status_code}"
        except (requests.RequestException, redis.RedisError) as e:
            # Handle exceptions
            return f"Error: {str(e)}"

    return wrapper


@count_access
def get_page(url: str) -> str:
    """Obtain the HTML content of `url` and return it."""
    return requests.get(url)
