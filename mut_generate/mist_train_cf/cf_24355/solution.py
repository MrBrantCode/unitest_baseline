"""
QUESTION:
Write a regular expression pattern to match any string that represents a valid email address. The pattern should match one or more non-space characters before the '@' symbol, one or more non-space characters after the '@' symbol and before the '.', and one or more non-space characters after the '.'. The pattern should be implemented in a way that it can be used in Python's re module.
"""

import re

def email_validator(email):
    """
    This function validates an email address using a regular expression pattern.
    
    Parameters:
    email (str): The email address to be validated.
    
    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    pattern = r"\S+@\S+\.\S+"
    return bool(re.match(pattern, email))