"""
QUESTION:
Construct a regex pattern named `pattern` that matches any string that starts with a lowercase letter followed by a digit and ends with three consecutive uppercase letters.
"""

import re

def pattern(string):
    """
    Returns True if the string starts with a lowercase letter followed by a digit and ends with three consecutive uppercase letters.
    
    Parameters:
    string (str): Input string
    
    Returns:
    bool: Whether the string matches the pattern
    """
    return bool(re.match(r"^[a-z][0-9].*[A-Z]{3}$", string))