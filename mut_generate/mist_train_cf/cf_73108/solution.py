"""
QUESTION:
Write a function `validate_zip(zip_code)` that takes a string `zip_code` as input and returns whether it is a valid United States postal zip code according to USPS guidelines, which requires the zip code to be either a 5-digit number or a 9-digit number in the format "nnnnn-nnnn" where 'n' denotes digit.
"""

import re

def validate_zip(zip_code):
    """
    Validate a United States postal zip code.

    Args:
    zip_code (str): The zip code to validate.

    Returns:
    bool: True if the zip code is valid, False otherwise.
    """
    zip_regex = r"^\d{5}(?:[-\s]\d{4})?$"
    return bool(re.search(zip_regex, zip_code))