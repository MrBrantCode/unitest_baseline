"""
QUESTION:
Create a function `validate_url(url)` that takes a URL string as input and returns `True` if the URL is valid, `False` otherwise. The function should validate URLs with protocols http, https, ftp, and ftps, as well as handle optional parts of a URL such as paths, query strings, and fragments. It should also ensure the URL has a properly formed subdomain, domain name, and top-level domain (TLD). The function should use regular expressions to match the URL.
"""

import re

def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return bool(regex.match(url))