"""
QUESTION:
Create a function named `get_even_characters` that takes a string as input and returns a new string containing only the alphabetic characters at even positions in the original string. The function should ignore non-alphabetic characters and maintain the original order of the characters. The function should use regular expressions.
"""

import re

def get_even_characters(string):
    """
    Returns a new string containing only the alphabetic characters at even positions in the original string.
    
    The function ignores non-alphabetic characters and maintains the original order of the characters.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    str: A new string containing only the alphabetic characters at even positions.
    """
    regex = r'[a-zA-Z]'
    matches = re.findall(regex, string)
    return ''.join([match for i, match in enumerate(matches) if i % 2 == 0])