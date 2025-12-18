"""
QUESTION:
Create a function named 'is_valid_zipcode' that takes a string as input and returns True if it matches a valid US zipcode, False otherwise. The function should match zipcodes that are exactly 5 digits or 9 digits with a hyphen after the 5th digit.
"""

import re

def is_valid_zipcode(zipcode):
    """
    This function checks if the input string is a valid US zipcode.
    
    A valid US zipcode is exactly 5 digits or 9 digits with a hyphen after the 5th digit.

    Parameters:
    zipcode (str): The input zipcode to be checked.

    Returns:
    bool: True if the zipcode is valid, False otherwise.
    """
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zipcode))