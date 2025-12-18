"""
QUESTION:
Write a regular expression pattern that matches strings which strictly start and end with exactly three capital letters immediately followed by exactly two lowercase letters. The function should not match any other characters before or after this pattern. The function name should be able to capture this requirement.
"""

import re

def entance(s):
    """
    This function checks if the input string strictly starts and ends with exactly three capital letters 
    immediately followed by exactly two lowercase letters.
    
    Parameters:
    s (str): Input string
    
    Returns:
    bool: True if the string matches the pattern, False otherwise
    """
    pattern = '^([A-Z]{3}[a-z]{2})$'
    return bool(re.match(pattern, s))