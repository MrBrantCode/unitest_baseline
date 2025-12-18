"""
QUESTION:
Create a function `is_valid_phone_number` that takes a string as input and returns True if the string represents a valid phone number, False otherwise. A valid phone number consists of 3 digits, optionally followed by a hyphen, then 3 more digits, optionally followed by a hyphen, and finally 4 digits.
"""

import re

def is_valid_phone_number(phone_number: str) -> bool:
    """
    Checks if the given string represents a valid phone number.
    
    A valid phone number consists of 3 digits, optionally followed by a hyphen, 
    then 3 more digits, optionally followed by a hyphen, and finally 4 digits.
    
    Args:
    phone_number (str): The phone number to check.
    
    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    pattern = re.compile(r"^[0-9]{3}-?[0-9]{3}-?[0-9]{4}$")
    return bool(pattern.match(phone_number))