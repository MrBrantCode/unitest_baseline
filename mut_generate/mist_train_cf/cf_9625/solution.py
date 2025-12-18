"""
QUESTION:
Write a function `validate_string_length_and_digits` to detect if a given string meets the following conditions: 
- The string must contain only digits (0-9). 
- The string length must be at least 5 characters and no more than 10 characters.
"""

import re

def validate_string_length_and_digits(s):
    """
    Validate if a given string contains only digits and its length is between 5 and 10.
    
    Args:
        s (str): The input string to be validated.
    
    Returns:
        bool: True if the string is valid, False otherwise.
    """
    pattern = r"^[0-9]{5,10}$"
    return bool(re.match(pattern, s))