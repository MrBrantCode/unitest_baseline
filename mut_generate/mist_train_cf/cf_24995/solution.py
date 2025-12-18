"""
QUESTION:
Write a function called `remove_duplicates` that takes a string as input and returns a string with any duplicate words removed, where duplicate words are defined as consecutive occurrences of the same word. The function should use regular expressions.
"""

import re

def remove_duplicates(sentence):
    """
    This function removes duplicate words from a given string.
    
    Args:
        sentence (str): The input string.
    
    Returns:
        str: A string with any duplicate words removed.
    """
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', sentence)