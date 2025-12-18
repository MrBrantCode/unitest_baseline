"""
QUESTION:
Construct a function `match_pattern` that takes a list of strings as input and returns a list of strings that match the regex pattern: a string starts with a lowercase letter followed by a digit and ends with three consecutive uppercase letters.
"""

import re

def match_pattern(strings):
    """
    Returns a list of strings that match the regex pattern: 
    a string starts with a lowercase letter followed by a digit and ends with three consecutive uppercase letters.

    Args:
    strings (list): A list of strings to check against the regex pattern.

    Returns:
    list: A list of strings that match the regex pattern.
    """
    pattern = r"^[a-z][0-9].*[A-Z]{3}$"
    return [string for string in strings if re.match(pattern, string)]