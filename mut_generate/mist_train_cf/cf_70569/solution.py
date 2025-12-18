"""
QUESTION:
Create a function named `check_url` that takes a string as input, representing a URL, and returns `True` if the URL has both a scheme (e.g., "http" or "https") and a network location (e.g., "www.example.com"), and `False` otherwise. The function should handle cases where the input is not a valid URL string.
"""

from urllib.parse import urlparse

def check_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False