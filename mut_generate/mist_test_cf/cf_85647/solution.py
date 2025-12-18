"""
QUESTION:
Create a function `check_symbols` that takes a string as input and returns `True` if the string contains both an exclamation mark `!` and a question mark `?` anywhere in the string, and `False` otherwise. The function should be case-sensitive and consider the presence of multiple `!` and `?` symbols.
"""

import re

def check_symbols(s):
    """
    This function checks if a given string contains both an exclamation mark and a question mark.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string contains both '!' and '?', False otherwise.
    """
    pattern = re.compile(r'.*!.*\?.*|.*\?.*!.*')
    return bool(pattern.match(s))