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
        if not cache.get("count:{}".format(url)):
            cache.set("count:{}".format(url), 1)
        else:
            cache.incr("count:{}".format(url), 1)
        cached_response = cache.get("response:{}".format(url))
        if cached_response:
            return str(cached_response)
        response = method(url)
        cache.setex("response:{}".format(url), 10, response)
        return response
    return wrapper


@count_access
def get_page(url: str) -> str:
    """Obtain the HTML content of `url` and returns it."""
    return requests.get(url).text
