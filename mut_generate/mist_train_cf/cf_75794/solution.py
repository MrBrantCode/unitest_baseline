"""
QUESTION:
Write a function `is_valid_us_zip(code)` that returns `True` if the given string represents a valid US postal zip code in either the basic five-digit format or the nine-digit 'ZIP+4' format, and `False` otherwise. The function should match the USPS standards and reject any undesired or invalid postal codes.
"""

import re

def is_valid_us_zip(code):
    pattern = re.compile("^\d{5}$|^\d{5}-\d{4}$")
    return bool(pattern.fullmatch(code))