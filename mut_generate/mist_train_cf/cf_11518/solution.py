"""
QUESTION:
Write a regular expression pattern to match a string that starts with 'hello', followed by one or more alphabetic characters, and ends with exactly two digits.
"""

import re

def entrance(s):
    """
    Checks if a string starts with 'hello', followed by one or more alphabetic characters, and ends with exactly two digits.

    Args:
    s (str): The input string to check.

    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    pattern = r"^hello[a-zA-Z]+[0-9]{2}$"
    return bool(re.match(pattern, s))