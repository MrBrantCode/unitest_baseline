"""
QUESTION:
Write a function `validate_string` that takes a string as input and returns `True` if the string contains only digits and does not end with a digit, and `False` otherwise. The function should accept any number of digits, including zero digits (i.e., an empty string), but should reject strings containing any non-digit character.
"""

import re

def validate_string(s):
    """
    Validate a string that contains only digits and does not end with a digit.

    Args:
        s (str): The input string to be validated.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    pattern = r"^\d*(?<!\d)$"
    return bool(re.match(pattern, s))