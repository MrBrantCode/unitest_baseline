"""
QUESTION:
Write a function `validate_string` that checks if a given alphanumeric string contains exactly two consecutive digits and at least one uppercase letter, with no special characters.
"""

import re

def validate_string(s):
    """
    Validate if the given alphanumeric string contains exactly two consecutive digits 
    and at least one uppercase letter, with no special characters.

    Args:
    s (str): The input string to be validated.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    pattern = r'^(?=.*\d{2})(?=.*[A-Z])[A-Za-z0-9]+$'
    return bool(re.match(pattern, s))