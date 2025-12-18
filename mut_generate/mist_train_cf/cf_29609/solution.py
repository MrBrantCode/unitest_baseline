"""
QUESTION:
Implement the function `validate_url(url)` that takes a string `url` as input and returns `True` if the URL matches the specified protocol, and `False` otherwise. The URL is valid if it meets the following conditions: 
- It starts with either "advert://" or "sqlfastadvert://".
- It is followed by a valid domain name, which consists of alphanumeric characters and periods, and ends with a port number (e.g., ":8080").
- The domain name must have at least one period and one alphanumeric character.
- The port number is optional, but if present, it must be a positive integer.
"""

import re

def validate_url(url: str) -> bool:
    protocol_pattern = r'(advert|sqlfastadvert)://'
    domain_pattern = r'([a-zA-Z0-9]+\.[a-zA-Z0-9.]+)'
    port_pattern = r'(:\d+)?'

    full_pattern = f'^{protocol_pattern}{domain_pattern}{port_pattern}$'

    return bool(re.match(full_pattern, url))