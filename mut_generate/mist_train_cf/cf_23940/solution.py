"""
QUESTION:
Create a function `validate_email` that takes a string as input and returns True if the string is a valid email address, False otherwise. A valid email address consists of alphanumeric characters before the '@' symbol, followed by alphanumeric characters, a '.', and then alphanumeric characters again. The function should be case-insensitive.
"""

import re

def validate_email(email):
    """
    Validate if the input string is a valid email address.
    
    Args:
    email (str): The email address to be validated.
    
    Returns:
    bool: True if the string is a valid email address, False otherwise.
    """
    
    pattern = r"^[a-z0-9]+@[a-z]+\.[a-z]+$"
    return bool(re.match(pattern, email, re.IGNORECASE))