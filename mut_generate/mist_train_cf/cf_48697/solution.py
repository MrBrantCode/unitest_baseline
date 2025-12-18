"""
QUESTION:
Create a function named `validate_url` that takes a string as input and returns `True` if the string is a valid URL and `False` otherwise. A valid URL should have a scheme (e.g., http, https) and a network location (e.g., www.google.com).
"""

from urllib.parse import urlparse

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False