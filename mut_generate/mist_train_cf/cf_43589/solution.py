"""
QUESTION:
Create a function `find_consecutive_xy` that takes a string `text` as input and returns all words containing the letters 'x' and 'y' appearing consecutively in them. The function should be case-sensitive and consider 'xy' and 'yx' as valid consecutive appearances.
"""

import re

def find_consecutive_xy(text):
    """
    This function takes a string as input and returns all words containing 
    the letters 'x' and 'y' appearing consecutively in them.

    Args:
        text (str): The input string.

    Returns:
        list: A list of words with consecutive 'x' and 'y'.
    """
    regex = re.compile(r'\b\w*(?:xy|yx)\w*\b')
    return regex.findall(text)