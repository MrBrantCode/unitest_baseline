"""
QUESTION:
Write a function `match_start_with_8` that takes a string as input and returns `True` if the string is a numerical expression that starts with the digit 8, and `False` otherwise. The numerical expression can be of any length and can contain any number of digits after the initial 8.
"""

import re

def match_start_with_8(s):
    """
    This function checks if a string is a numerical expression that starts with the digit 8.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string is a numerical expression that starts with the digit 8, False otherwise.
    """
    pattern = re.compile(r'^8\d*')
    return bool(pattern.match(s))