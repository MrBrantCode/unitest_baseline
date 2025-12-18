"""
QUESTION:
Write a function `verify_pattern` that takes a string as input and returns `True` if the string matches the following pattern, and `False` otherwise: one or more digits, optionally surrounded by whitespace, followed by a hyphen, followed by one or more digits, also optionally surrounded by whitespace, with no other characters present apart from the optional whitespace. The function should use a regular expression to verify the pattern.
"""

import re

def verify_pattern(s):
    """
    Verify if the input string matches the pattern: 
    one or more digits, optionally surrounded by whitespace, 
    followed by a hyphen, followed by one or more digits, 
    also optionally surrounded by whitespace, with no other 
    characters present apart from the optional whitespace.
    
    Parameters:
    s (str): The input string to be verified
    
    Returns:
    bool: True if the string matches the pattern, False otherwise
    """
    pattern = re.compile(r'^\s*\d+\s*-\s*\d+\s*$')
    return bool(pattern.match(s))