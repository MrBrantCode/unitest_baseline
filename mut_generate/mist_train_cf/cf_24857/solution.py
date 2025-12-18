"""
QUESTION:
Write a function `detect_email` that takes a string as input and returns a boolean indicating whether the string is a valid email address. The function should use regular expressions to match the input string against a pattern that represents a typical email address format. The email address should consist of one or more alphanumeric characters, dots, or underscores, followed by '@', then one or more alphanumeric characters, dots, or underscores, and finally a top-level domain with 2-3 characters.
"""

import re

def detect_email(email):
    """
    This function checks if the input string is a valid email address.
    
    Args:
        email (str): The input string to be checked.
    
    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """
    pattern = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    return bool(re.match(pattern, email))