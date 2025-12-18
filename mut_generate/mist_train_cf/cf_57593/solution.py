"""
QUESTION:
Create a function called `remove_punctuation` that takes a string as input and returns a new string with all punctuation symbols removed. Use regular expressions in Python to achieve this, and note that the function should only return a string containing letters, numbers, and whitespace characters.
"""

import re

def remove_punctuation(text_string):
    """
    Removes all punctuation symbols from a given string.
    
    Args:
    text_string (str): The input string to remove punctuation from.
    
    Returns:
    str: A new string with all punctuation symbols removed.
    """
    return re.sub(r'[^\w\s]', '', text_string)