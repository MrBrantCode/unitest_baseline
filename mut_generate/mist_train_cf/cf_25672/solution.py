"""
QUESTION:
Write a function to match any string containing only the letters 'a' and 'b'. The function should return True if the string consists entirely of 'a's and 'b's, and False otherwise.
"""

import re

def match_ab(s):
    """
    Returns True if the string consists entirely of 'a's and 'b's, False otherwise.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string consists entirely of 'a's and 'b's, False otherwise.
    """
    pattern = re.compile('^[ab]+$')
    return bool(pattern.match(s))