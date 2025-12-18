"""
QUESTION:
Create a function `validate_string` that takes a string as input and returns `True` if the string starts with a lowercase letter, contains at least one digit, and ends with a special character, and `False` otherwise. The special character is any character that is not a letter or a digit.
"""

import re

def validate_string(s):
    """
    Validate a string based on certain conditions.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string is valid, False otherwise.

    A string is valid if it starts with a lowercase letter, contains at least one digit, and ends with a special character.
    """
    pattern = r"^[a-z].*[0-9].*[^a-zA-Z0-9]$"
    return bool(re.match(pattern, s))