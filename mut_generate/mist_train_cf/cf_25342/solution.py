"""
QUESTION:
Write a function `is_valid_email` that takes a string as input and returns `True` if the string is a valid email address, and `False` otherwise. A valid email address should contain the "@" symbol and at least one period (.) in the domain name.
"""

import re

def is_valid_email(email):
    """
    Checks if a given string is a valid email address.
    
    A valid email address should contain the "@" symbol and at least one period (.) in the domain name.
    
    Parameters:
    email (str): The input string to be checked.
    
    Returns:
    bool: True if the string is a valid email address, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))