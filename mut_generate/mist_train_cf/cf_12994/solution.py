"""
QUESTION:
Write a function `find_carrot_pattern` that uses regular expression to search for the pattern "carrot" followed by a number between 1 and 10 in a given string. The function should return True if the pattern exists and False otherwise. The regular expression should match "carrot" as a separate word and ensure the number is also a separate word.
"""

import re

def find_carrot_pattern(s):
    """
    Searches for the pattern "carrot" followed by a number between 1 and 10 in a given string.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the pattern exists, False otherwise.
    """
    pattern = r'\bcarrot\b(?:\s*(?:[1-9]|10))\b'
    return bool(re.search(pattern, s))