"""
QUESTION:
Create a function `is_valid_url` that determines if a given string is a valid URL. The function should return `True` if the string matches the URL pattern, and `False` otherwise. The URL pattern should match most common URLs, including those with or without 'www', HTTP, or HTTPS.
"""

import re

def is_valid_url(url):
    pattern = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
    return bool(re.match(pattern, url))