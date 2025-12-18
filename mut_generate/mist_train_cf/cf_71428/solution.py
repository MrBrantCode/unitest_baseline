"""
QUESTION:
Create a function `check_string(string)` that uses regular expressions to check if a given string contains both "hello" and "world" anywhere in the string, in any order, without considering the case sensitivity (i.e., it should match "hello", "Hello", "HELLO", etc.).
"""

import re

def check_string(string):
    """
    This function checks if a given string contains both "hello" and "world" anywhere in the string, 
    in any order, without considering the case sensitivity.

    Args:
        string (str): The input string to be checked.

    Returns:
        bool: True if the string contains both "hello" and "world", False otherwise.
    """
    pattern = r"(?=.*hello)(?=.*world)"
    return bool(re.search(pattern, string, re.IGNORECASE))