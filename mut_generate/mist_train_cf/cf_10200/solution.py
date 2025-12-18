"""
QUESTION:
Create a function `validate_url` that takes a string as input and returns `True` if it matches a URL that starts with "https://" and ends with ".com", contains at least one subdomain before the top-level domain, and may contain any combination of alphanumeric characters, dashes, and dots in between, and `False` otherwise. The function should return the result in a boolean value.
"""

import re

def validate_url(url):
    pattern = r'^(https:\/\/)([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\.com$'
    return bool(re.match(pattern, url))