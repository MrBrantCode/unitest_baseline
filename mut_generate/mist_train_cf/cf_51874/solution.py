"""
QUESTION:
Create a function named `validate_usps` that takes two parameters: a string and a boolean indicating whether the string is a zip code or not. The function should return `True` if the string is valid and `False` otherwise. A valid string can be either a USPS compliant 5 or 9 digit zip code or a valid 2-letter state abbreviation. The function should handle boundary scenarios and exceptions. Note that city names are not included in the validation.
"""

import re

# USPS compliant Zip Codes Regular expression
zip_code_regex = "^\d{5}(?:[-\s]\d{4})?$"

# USPS Compliant states abbreviations List
state_abbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def validate_usps(string, is_zip_code):
    """
    Validate a USPS compliant string.

    Args:
    string (str): The input string to be validated.
    is_zip_code (bool): A boolean indicating whether the string is a zip code or not.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    if is_zip_code:
        return bool(re.fullmatch(zip_code_regex, string))
    else:
        return string in state_abbreviations