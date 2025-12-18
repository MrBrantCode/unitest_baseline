"""
QUESTION:
Create a function `is_valid_url(url)` that checks if a given URL matches the structure `https://www.example.com/path/page.html`. The function should return `True` if the URL is valid and `False` otherwise. The URL structure should have `https://www.` followed by one or more word characters, dots, or hyphens, then a slash, one or more word characters, another slash, one or more word characters, and end with `.html`.
"""

import re

def is_valid_url(url):
    pattern = re.compile(r'https://www\.[\w.-]+/\w+/\w+\.html$')
    return re.match(pattern, url) is not None