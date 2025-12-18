"""
QUESTION:
Construct a regular expression to match a string representing a valid phone number in the format XXX-XXX-XXXX, where X is a digit (0-9). The regex should match the entire string, not just a part of it, and the phone number should be in the exact format with hyphens between the digit groups.
"""

import re

def entrance(s):
    """
    Checks if a given string represents a valid phone number in the format XXX-XXX-XXXX.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a valid phone number, False otherwise.
    """
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, s))