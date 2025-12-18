"""
QUESTION:
Write a function `count_alphanumeric` that takes a string as input and returns the number of alphanumeric characters in the string, excluding any punctuation marks or special characters. The function should only count characters that are either letters (a-z or A-Z) or numbers (0-9).
"""

import re

def count_alphanumeric(input_string):
    """
    Returns the number of alphanumeric characters in the input string.

    Args:
    input_string (str): The input string.

    Returns:
    int: The count of alphanumeric characters.
    """
    clean_string = re.sub(r'\W+', '', input_string)  # Remove punctuation marks and special characters
    return sum(1 for char in clean_string if char.isalnum())