"""
QUESTION:
Create a function `validate_string` that takes a string as input and returns `True` if the string consists of lowercase letters "a" through "e" with no consecutive duplicates and has a length of exactly 5 characters, and `False` otherwise.
"""

import re

def validate_string(s):
    """
    This function validates a string if it consists of lowercase letters "a" through "e" 
    with no consecutive duplicates and has a length of exactly 5 characters.

    Parameters:
    s (str): The input string.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    pattern = r'^(?!.*([a-e])\1)[a-e]{5}$'
    return bool(re.match(pattern, s))