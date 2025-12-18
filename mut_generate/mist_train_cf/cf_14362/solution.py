"""
QUESTION:
Create a function `has_consecutive_digits` that takes a string as input and returns True if the string contains exactly two consecutive digits, and False otherwise. The function should use a regex pattern to achieve this.
"""

import re

def has_consecutive_digits(s):
    """
    Checks if a string contains exactly two consecutive digits.
    
    Args:
        s (str): The input string.
    
    Returns:
        bool: True if the string contains exactly two consecutive digits, False otherwise.
    """
    return bool(re.search(r'\d{2}', s))