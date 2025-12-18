"""
QUESTION:
Write a function `check_string` that takes a string as input and returns True if the string is at least 6 characters long and contains at least one number followed by a letter, and False otherwise.
"""

import re

def check_string(s):
    """
    Returns True if the string is at least 6 characters long and contains at least one number followed by a letter, and False otherwise.
    
    Parameters:
    s (str): The input string
    
    Returns:
    bool: Whether the string meets the specified criteria
    """
    return bool(re.match(r'^(?=.*\d)[a-zA-Z0-9]{6,}$', s))