"""
QUESTION:
Create a function `normalize_string` that takes an input string, removes any special characters or punctuation marks, and converts the remaining characters to lowercase while preserving the order of the characters. The output string should only include lowercase letters and numbers.
"""

import re

def normalize_string(s):
    """
    Removes special characters or punctuation marks from the input string and 
    converts the remaining characters to lowercase while preserving the order of the characters.

    Args:
        s (str): The input string to be normalized.

    Returns:
        str: The normalized string with only lowercase letters and numbers.
    """
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    return s.lower()