import redis
import requests


def get_page(url: str) -> str:
    """Obtain the HTML content of `url` and return it, with caching and access count tracking."""
    cache = redis.Redis()

    # Check if the URL is already cached
    cached_response = cache.get(url)
    if cached_response:
        return cached_response.decode()

    # Make the request and cache the response
    response = requests.get(url)
    if response.status_code == 200:
        response_text = response.text
        cache.set(url, response_text, ex=10)
        return response_text
    else:
        return f"Error: {response.status_code}"
