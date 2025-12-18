"""
QUESTION:
Create a function named `detect_start_with_8` that takes a string as input and returns True if the string represents a numerical value that starts with the digit 8, and False otherwise. The function should use a regular expression pattern to match the input string.
"""

import re

def detect_start_with_8(s):
    """
    Returns True if the input string represents a numerical value that starts with the digit 8, and False otherwise.
    
    Args:
        s (str): Input string to be checked.
    
    Returns:
        bool: Whether the string represents a numerical value starting with the digit 8.
    """
    pattern = r'^8\d*$'
    return bool(re.search(pattern, s))