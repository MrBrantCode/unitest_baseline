"""
QUESTION:
Create a function `validate_url(url)` that takes a URL string as input and returns True if the URL is valid, False otherwise. A valid URL must start with 'https://', end with '.com', and have one or more subdomains. The URL must not contain query or fragment identifiers.
"""

import re

def validate_url(url):
    pattern = r'^https://([a-zA-Z0-9-]+\.)+[a-zA-Z0-9-]+\.com$'
    match = re.match(pattern, url)

    return match is not None