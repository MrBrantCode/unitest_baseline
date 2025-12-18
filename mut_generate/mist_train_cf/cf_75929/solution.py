"""
QUESTION:
Create a Python function `is_uppercase_alphanumeric` that uses a regular expression pattern to check if a given string consists only of uppercase English alphabets and numerical digits. The function should return `True` if the string matches the pattern and `False` otherwise. The pattern should work for cases where either uppercase alphanumeric characters or numerical digits dominate the string.
"""

import re

def is_uppercase_alphanumeric(s):
    """
    Checks if a given string consists only of uppercase English alphabets and numerical digits.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    pattern = r"^[A-Z0-9]+$"
    return bool(re.match(pattern, s))