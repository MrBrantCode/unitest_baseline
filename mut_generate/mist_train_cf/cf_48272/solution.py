"""
QUESTION:
Write a function `is_valid_url(url)` that checks if a given string `url` conforms to the standard format of a Uniform Resource Locator (URL). The function should return `True` if the URL is valid and `False` otherwise. The function should support both HTTP and HTTPS protocols, as well as URLs with and without the protocol prefix (e.g., "http://www.google.com" and "www.google.com"). The function should not rely on external libraries other than the built-in Python `re` library for regular expressions.
"""

import re

def is_valid_url(url):
    # Regex to check URL
    regex = re.compile(
        r'^(http://|https://)?'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?'  # domain
        r'|(?:\d{1,3}\.){3}\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
    # Return whether the url passes the check of the regex
    return re.match(regex, url) is not None