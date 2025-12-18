"""
QUESTION:
Write a function called `validate_url(url)` that takes a Uniform Resource Locator (URL) as input and returns `True` if the URL is valid and `False` otherwise. The function should use a regular expression (regex) pattern to validate the URL. The regex pattern should cover standard domain structures, local hosts, IP addresses, and optional ports. The function should be case-insensitive.
"""

import re

def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None