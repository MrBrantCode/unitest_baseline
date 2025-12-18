"""
QUESTION:
Write a function `is_divisible_by_3` that takes a string as input and returns a boolean indicating whether the integer represented by the string is divisible by 3. The input string will contain only digits. The function should use regular expressions.
"""

import re

def is_divisible_by_3(s):
    """
    Returns a boolean indicating whether the integer represented by the string is divisible by 3.
    
    Args:
        s (str): A string containing only digits.
    
    Returns:
        bool: Whether the integer represented by the string is divisible by 3.
    """
    return re.match(r"^[0-9]*(3|6|9)$", s) is not None