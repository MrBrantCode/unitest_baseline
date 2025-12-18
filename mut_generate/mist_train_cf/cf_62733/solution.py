"""
QUESTION:
Write a function named `match_url` that takes a URL as input and returns `True` if it matches the following criteria and `False` otherwise: 
- The URL starts with 'http://' or 'https://'.
- The URL contains at least one subdomain.
- The URL does not contain any hyphens or numbers.
- The URL ends with '.net'.
"""

import re

def match_url(url):
    pattern = r'^https?:\/\/([a-z]+\.)+[a-z]+\.net$'
    if re.match(pattern, url):
        return True
    return False