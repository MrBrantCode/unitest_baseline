"""
QUESTION:
Write a function named `is_valid_url` that takes a string as input and returns `True` if the string is a valid URL, and `False` otherwise. A valid URL must contain both a scheme (e.g. "http" or "https") and a network location (the domain name). The function should not check if the URL leads to a valid, reachable website, or if the domain exists.
"""

from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False