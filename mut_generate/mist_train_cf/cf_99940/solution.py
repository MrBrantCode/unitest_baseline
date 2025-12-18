"""
QUESTION:
Create a function named `normalize_string` that takes an input string as an argument. The function should return a new string that only includes lower case letters and numbers from the original string, preserving the order of the characters, and removing any special characters or punctuation marks.
"""

import re

def normalize_string(s):
    """
    Normalize a given string by removing special characters and punctuation marks, 
    preserving only lower case letters and numbers, and maintaining the original order.

    Args:
        s (str): The input string to be normalized.

    Returns:
        str: The normalized string.
    """
    # Remove special characters and punctuation marks
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    # Convert all remaining characters to lowercase
    s = s.lower()
    return s