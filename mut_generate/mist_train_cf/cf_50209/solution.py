"""
QUESTION:
Create a function `remove_special_chars_and_numbers` that takes a string as input, replaces all numbers and special characters with a single space, and returns the resulting string.
"""

import re

def remove_special_chars_and_numbers(sentence):
    """
    Replaces all numbers and special characters in the input string with a single space.
    
    Args:
        sentence (str): The input string.
    
    Returns:
        str: The resulting string after replacing numbers and special characters.
    """
    return re.sub(r"[^a-zA-Z]+", " ", sentence)