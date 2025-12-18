"""
QUESTION:
Write a function called `match_email` that validates if a given string is a valid email address. The email address should start with one or more alphanumeric characters, followed by the "@" symbol, and then followed by one or more alphanumeric characters.
"""

import re

def match_email(s):
    """
    Validates if a given string is a valid email address.
    
    The email address should start with one or more alphanumeric characters, 
    followed by the "@" symbol, and then followed by one or more alphanumeric characters.

    Args:
        s (str): The input string to be validated.

    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """
    pattern = r'^\w+@\w+$'
    return bool(re.match(pattern, s))