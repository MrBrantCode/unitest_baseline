"""
QUESTION:
Create a function named `validate_string` that takes a string as input and returns `True` if the string contains only lowercase English letters and has a minimum length of 5 characters, and `False` otherwise.
"""

import re

def validate_string(s):
    """
    Validate if the input string contains only lowercase English letters and has a minimum length of 5 characters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    bool: True if the string is valid, False otherwise.
    """
    pattern = r'^[a-z]{5,}$'
    return bool(re.match(pattern, s))