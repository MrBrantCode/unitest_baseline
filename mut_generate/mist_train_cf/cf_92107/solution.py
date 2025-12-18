"""
QUESTION:
Create a regular expression pattern named "consecutive_digits" that matches a string of consecutive numbers with a minimum of 4 digits. The string should not contain any whitespace characters. The pattern should match the entire string from start to end, without any preceding or trailing characters.
"""

import re

def consecutive_digits(s):
    """
    Checks if the input string consists of consecutive digits with a minimum of 4 digits.
    
    Args:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string consists of consecutive digits with a minimum of 4 digits, False otherwise.
    """
    pattern = r"^\d{4,}$"
    return bool(re.match(pattern, s))