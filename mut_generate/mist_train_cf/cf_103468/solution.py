"""
QUESTION:
Write a function `split_string_into_words` that takes a string as input and returns a list of words that only contain letters, excluding any words that contain numbers or special characters. The function should split the input string into words and filter out words with non-alphabet characters.
"""

import re

def split_string_into_words(s):
    """
    This function splits the input string into words and filters out words with non-alphabet characters.
    
    Args:
        s (str): The input string to be processed.
    
    Returns:
        list: A list of words that only contain letters.
    """
    return re.findall(r'\b[a-zA-Z]+\b', s)