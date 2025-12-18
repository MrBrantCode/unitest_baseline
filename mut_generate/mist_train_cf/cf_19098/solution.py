"""
QUESTION:
Write a function `match_five_consecutive_digits` that takes a string as input and returns `True` if the string contains a sequence of exactly five consecutive digits, and `False` otherwise. The function should consider a sequence of digits as part of a larger number or word if they are not separated by non-digit characters.
"""

import re

def match_five_consecutive_digits(s: str) -> bool:
    """
    Checks if a string contains a sequence of exactly five consecutive digits.

    Args:
    s (str): The input string to check.

    Returns:
    bool: True if the string contains a sequence of exactly five consecutive digits, False otherwise.
    """
    pattern = r'\b\d{5}\b'
    return bool(re.search(pattern, s))