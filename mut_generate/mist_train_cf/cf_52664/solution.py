"""
QUESTION:
Create a function `match_pattern` that takes a string as input and returns `True` if the string matches the pattern of a lowercase letter 'w' between 'a' and 'c', followed by a digit 'x' between 0 and 9, then any lowercase letter 'y', and finally any uppercase letter 'z'. The string should be exactly 4 characters long.
"""

import re

def match_pattern(string):
    """
    Returns True if the string matches the pattern of a lowercase letter 'w' between 'a' and 'c', 
    followed by a digit 'x' between 0 and 9, then any lowercase letter 'y', and finally any uppercase letter 'z'. 
    The string should be exactly 4 characters long.

    Args:
    string (str): The input string to be checked.

    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    pattern = r'^[a-c][0-9][a-z][A-Z]$'
    return bool(re.match(pattern, string))