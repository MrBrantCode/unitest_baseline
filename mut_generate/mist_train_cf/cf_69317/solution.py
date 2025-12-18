"""
QUESTION:
Write a function `find_xy_pattern` that takes a string `text` as input and returns a list of words containing the sequence 'xy' in any position (beginning, middle, or end). The function should be case-insensitive and only match words that have 'x' immediately followed by 'y' with any letters before and/or after them.
"""

import re

def find_xy_pattern(text):
    """
    Find all words containing the sequence 'xy' in any position.
    
    Args:
    text (str): The input text.
    
    Returns:
    list: A list of words containing 'xy'.
    """
    # Regular expression pattern to match words with 'xy'
    pattern = r'\b[a-zA-Z]*xy[a-zA-Z]*\b'
    
    # Find all matches in the string and convert to lower case
    matches = [match.lower() for match in re.findall(pattern, text, flags=re.IGNORECASE)]
    
    return matches