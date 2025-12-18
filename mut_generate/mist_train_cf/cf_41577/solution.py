"""
QUESTION:
Implement a function `get_asin(url)` that takes a string `url` as input. The function should extract and return the ASIN (Amazon Standard Identification Number) if the URL is a valid Amazon product URL and the ASIN is present. If the URL is not a valid Amazon product URL or if the ASIN is not present, the function should raise an `AsinNotFoundException`.
"""

import re

class AsinNotFoundException(Exception):
    pass

def get_asin(url):
    if not url.startswith("https://www.amazon."):
        raise AsinNotFoundException("Invalid Amazon URL")

    asin_match = re.search(r'/([A-Z0-9]{10})(?:[/?]|$)', url)
    if asin_match:
        return asin_match.group(1)
    else:
        raise AsinNotFoundException("ASIN not found in the URL")