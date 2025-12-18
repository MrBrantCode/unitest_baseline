"""
QUESTION:
Write a function named `verify_url` that takes a string `url` as input and returns `True` if the string is a valid URL and `False` otherwise. A valid URL must contain a scheme (protocol) and a network location (host).
"""

from urllib.parse import urlparse

def verify_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False