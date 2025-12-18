"""
QUESTION:
Create a function `url_validator` that takes a string `url` as input and returns `True` if the URL is valid, `False` otherwise. The function should validate URLs with or without protocol (http, https, ftp), with or without 'www', and with various top-level domains (gTLDs, country code TLDs, new TLDs). The function should also validate IP addresses and ports. The input `url` can be a string representing a URL. The function should return a boolean indicating whether the URL is valid or not.
"""

import re

def url_validator(url):
    pattern = re.compile(
        r'^(?:http|ftp|https)?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(pattern, url) is not None