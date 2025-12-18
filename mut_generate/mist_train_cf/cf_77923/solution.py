"""
QUESTION:
Construct a regex pattern, `detect_ampersand`, that matches any string where the ampersand character (&) is the first character. The pattern should match any string of any length as long as it starts with an ampersand.
"""

import re

def detect_ampersand(s):
    """
    This function checks if the input string starts with an ampersand character (&).
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string starts with an ampersand, False otherwise.
    """
    pattern = re.compile(r'^&.*')
    return bool(pattern.match(s))