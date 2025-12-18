"""
QUESTION:
Write a function called `validate_phone_number` that takes a string as input and returns True if it matches a valid phone number format and False otherwise. A valid phone number consists of an area code starting with "1" and consisting of exactly three digits, followed by a hyphen ("-"), followed by a three-digit phone number, followed by a hyphen ("-"), followed by a four-digit phone number. The pattern should also allow for optional parentheses around the area code and a space or a dot as separators between the digits of the three-digit and four-digit phone numbers.
"""

import re

def validate_phone_number(phone_number):
    """
    Validate a given phone number.
    
    Args:
    phone_number (str): The phone number to validate.
    
    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    pattern = r'^(?:(?:\(1\d{2}\)|1\d{2})[-.])?\d{3}[-.]\d{4}$'
    return bool(re.match(pattern, phone_number))