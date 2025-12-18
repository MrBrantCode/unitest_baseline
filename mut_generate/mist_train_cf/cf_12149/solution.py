"""
QUESTION:
Write a function called `match_string_pattern` that takes two parameters, a string and a regular expression pattern, and returns a boolean indicating whether the string matches the pattern. The pattern may contain nested groups.
"""

import re

def match_string_pattern(string, pattern):
    """
    This function checks if a given string matches a regular expression pattern.
    
    Args:
    string (str): The string to be checked.
    pattern (str): The regular expression pattern.
    
    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    try:
        return bool(re.fullmatch(pattern, string))
    except re.error:
        return False