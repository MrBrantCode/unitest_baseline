"""
QUESTION:
Write a function named `is_url_valid` that takes a string as input and returns a boolean indicating whether the string is a valid Uniform Resource Locator (URL). The function should use the built-in URL parsing library of the programming language. If the string is a valid URL, the function should return `True`; otherwise, it should return `False`.
"""

from urllib.parse import urlparse

def is_url_valid(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False