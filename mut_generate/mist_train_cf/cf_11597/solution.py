"""
QUESTION:
Create a function `match_catdog` that takes a string as input and returns a boolean indicating whether the string starts with "cat", ends with "dog", and contains only lowercase letters. The function should match whole words only, excluding strings that are part of a larger word.
"""

import re

def match_catdog(s):
    """
    Returns True if the string starts with "cat", ends with "dog", and contains only lowercase letters.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    pattern = r'\bcat[a-z]*dog\b'
    return bool(re.fullmatch(pattern, s, re.IGNORECASE))