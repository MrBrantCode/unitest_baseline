"""
QUESTION:
Design a regex pattern to match a valid URL. The function should be named `is_valid_url`. The URL can be either HTTP or HTTPS, should contain at least two alphabetic characters after the top-level domain, and can have an optional path. The pattern should be case-insensitive and can include alphanumeric characters, periods, hyphens, and forward slashes.
"""

import re

def is_valid_url(url):
    pattern = r'^(https?:\/\/)[\da-z\.-]+\.[a-z\.]{2,}\/?[\/\w \.-]*$'
    return bool(re.match(pattern, url, re.IGNORECASE))