"""
QUESTION:
Create a function named `is_valid_zipcode` that takes a string as input and returns `True` if the string represents a valid United States postal zip code and `False` otherwise. A valid United States postal zip code is either a five-digit code or a nine-digit code (zip+4) where the first five digits represent the zip code and the last four digits represent the zip+4 extension, separated by a hyphen.
"""

import re

def is_valid_zipcode(zipcode):
    pattern = re.compile("^\d{5}(?:-\d{4})?$")
    if pattern.match(zipcode):
        return True
    else:
        return False