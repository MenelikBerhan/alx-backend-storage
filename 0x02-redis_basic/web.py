import redis
import requests
from typing import Dict


def get_page(url: str) -> str:
    """Obtain the HTML content of `url` and return it, with caching and access
    count tracking."""
    cache = redis.Redis()

    # Check if the URL is already cached
    cached_response = cache.get(url)
    if cached_response:
        return cached_response.decode()

    # Increment the access count for the URL
    access_count_key = f'count:{url}'
    access_count = cache.incr(access_count_key, 1)

    if access_count == 1:
        # Make the request and cache the response if it's the first access
        response = requests.get(url)
        if response.status_code == 200:
            response_text = response.text
            cache.set(url, response_text, ex=10)
            return response_text
        else:
            return f"Error: {response.status_code}"
    else:
        # Return an error message if the URL was accessed before but not cached
        return "Error: URL already accessed before but not cached."
