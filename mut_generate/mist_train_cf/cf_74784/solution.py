"""
QUESTION:
Write a Python function named `regex_match` that takes a regular expression `pattern` and a `string` as inputs, and returns `True` if the `string` matches the `pattern`, `False` if not, and an error message if the `pattern` is invalid. The function should handle edge cases such as empty patterns, empty strings, and non-string inputs.
"""

import re

def regex_match(pattern, string):
    """
    Checks if a given string matches a regular expression pattern.
    
    Args:
        pattern (str): The regular expression pattern to match.
        string (str): The string to check for a match.
    
    Returns:
        bool or str: True if the string matches the pattern, False if not, 
                     and an error message if the pattern is invalid.
    """
    
    # Check that pattern and string are strings
    if not isinstance(pattern, str) or not isinstance(string, str):
        return "Pattern and string must be strings"
    
    # Handle the case of an empty pattern
    if pattern == "":
        if string == "":
            return True
        else:
            return False
    
    # Check for a valid pattern
    try:
        re.compile(pattern)
    except re.error:
        return "Invalid regular expression pattern"
    
    # Perform the search
    if re.search(pattern, string):
        return True
    else:
        return False