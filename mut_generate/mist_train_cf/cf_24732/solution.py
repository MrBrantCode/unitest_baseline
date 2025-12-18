"""
QUESTION:
Create a function `is_valid_phone_number` that takes a string as input and returns `True` if it matches a valid U.S. phone number format, and `False` otherwise. A valid U.S. phone number consists of exactly 10 digits, and may be formatted with dashes or parentheses as separators.
"""

import re

def is_valid_phone_number(phone_number):
    """
    This function checks if the input string matches a valid U.S. phone number format.
    
    A valid U.S. phone number consists of exactly 10 digits, and may be formatted 
    with dashes or parentheses as separators.
    
    Parameters:
    phone_number (str): The input phone number string to be validated.
    
    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    pattern = re.compile(r'^\d{10}$|^\d{3}-\d{3}-\d{4}$|^\(\d{3}\) \d{3}-\d{4}$')
    return bool(pattern.match(phone_number))