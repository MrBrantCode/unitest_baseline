"""
QUESTION:
Create a function `normalize_string` that takes a string as input and returns the normalized string with only lowercase letters and numbers, while preserving the order of the characters. The function should remove any special characters or punctuation marks from the original string.
"""

import re

def normalize_string(s):
    """
    This function takes a string as input and returns the normalized string 
    with only lowercase letters and numbers, while preserving the order of the characters.

    Args:
        s (str): The input string to be normalized.

    Returns:
        str: The normalized string.
    """
    # Remove special characters and punctuation marks
    # and convert all remaining characters to lowercase
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()