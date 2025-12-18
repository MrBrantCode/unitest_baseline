"""
QUESTION:
Create a function `find_consecutive_xy` that takes a string as input and returns a list of words containing the letters 'x' and 'y' consecutively. The function should use regular expressions to match the pattern.
"""

import re

def find_consecutive_xy(input_string):
    """
    This function takes a string as input and returns a list of words containing the letters 'x' and 'y' consecutively.
    
    Args:
        input_string (str): The input string to search for words with consecutive 'x' and 'y'.
    
    Returns:
        list: A list of words with consecutive 'x' and 'y'.
    """
    
    # Regular expression to find words with 'x' and 'y' appearing consecutively
    pattern = re.compile(r'\b\w*xy\w*\b')
    
    # Find all matches in the input string
    matches = pattern.findall(input_string)
    
    return matches