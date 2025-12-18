"""
QUESTION:
Write a function called `validate_string` that takes a string as input and returns a boolean indicating whether the string meets the following conditions:
- contains at least one uppercase letter, one lowercase letter, and one number
- is at least 6 characters long
- does not contain the words "password" or "credit card"
The function should be able to handle strings in multiple languages.
"""

import re

def validate_string(s):
    """
    Validate if a string meets the following conditions:
    - contains at least one uppercase letter, one lowercase letter, and one number
    - is at least 6 characters long
    - does not contain the words "password" or "credit card"
    
    Args:
        s (str): Input string
    
    Returns:
        bool: Whether the string is valid or not
    """
    regex_pattern = r"(?!.*(?:password|credit card))(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{6,}"
    return bool(re.match(regex_pattern, s))