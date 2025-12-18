"""
QUESTION:
Design a function named `validate_url` that accepts a URL string as input. The function should verify that the URL starts with either 'http' or 'https', contains a non-www domain, has no invalid characters, and is in a valid format. If the URL is valid, the function should parse the URL and return its domain and page path as separate elements. If the URL is invalid, the function should return a message saying "Invalid url".
"""

import re
from urllib.parse import urlparse

def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    result = re.match(regex, url)
    
    if not result:
        return "Invalid url"
    else:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        path = parsed_url.path
        return domain, path