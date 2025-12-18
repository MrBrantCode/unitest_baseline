"""
QUESTION:
Create a function called `split_string` that takes a string as input and returns two lists of strings. The first list should contain individual words as elements, and the second list should contain individual characters. The function should accommodate accented characters, punctuation marks, and the absence of spaces. The order of word appearance in the original string should be preserved.
"""

import re

def split_string(s):
    """
    This function splits a given string into two lists.
    The first list contains individual words as elements, 
    and the second list contains individual characters.
    
    Parameters:
    s (str): The input string
    
    Returns:
    tuple: A tuple of two lists. The first list contains individual words, 
    and the second list contains individual characters.
    """
    words = re.findall(r'\w+', s)
    chars = list(s)
    return words, chars