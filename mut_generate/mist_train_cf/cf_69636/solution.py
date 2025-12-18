"""
QUESTION:
Create a function `is_valid_url` that checks if a given string is a valid URL following the standard format of `http` or `https` protocol, a domain or IP address, an optional port, and a path. The function should return `True` if the URL is valid and `False` otherwise. 

The URL format should include: 
- `http` or `https` protocol
- a domain (with at least two characters top-level domain) or IP address
- an optional port
- a path (can be empty)

Note: The function should not check if the URL actually exists or points to a reachable resource on the Internet.
"""

import re

def is_valid_url(url):
    """
    Checks if a given string is a valid URL following the standard format of 
    `http` or `https` protocol, a domain or IP address, an optional port, and a path.
    
    Args:
        url (str): The URL to be checked.
    
    Returns:
        bool: True if the URL is valid, False otherwise.
    """

    url_regex = re.compile(
        r'http[s]?://' # http or https
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain
        r'localhost|' # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # or IP
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return bool(url_regex.match(url))