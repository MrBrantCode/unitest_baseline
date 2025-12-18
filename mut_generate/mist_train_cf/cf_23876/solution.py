"""
QUESTION:
Write a regular expression function `check_string` that checks if the input string matches the pattern of an uppercase letter followed by at least 4 digits. The function should return `True` if the string matches the pattern and `False` otherwise.
"""

import re

def check_string(s):
    """
    Checks if the input string matches the pattern of an uppercase letter followed by at least 4 digits.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    pattern = r"^[A-Z]\d{4,}$"
    return bool(re.match(pattern, s))