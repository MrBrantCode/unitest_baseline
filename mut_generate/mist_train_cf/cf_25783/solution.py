"""
QUESTION:
Create a function `validate_password` that checks if a given password string meets the following conditions: it must contain at least one uppercase character, one lowercase character, and one digit. The function should return a boolean value indicating whether the password is valid or not.
"""

import re

def validate_password(password: str) -> bool:
    """
    Validate a password.
    
    The password is valid if it contains at least one uppercase character, 
    one lowercase character, and one digit.
    
    Args:
    password (str): The password to be validated.
    
    Returns:
    bool: True if the password is valid, False otherwise.
    """
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'
    return bool(re.match(pattern, password))