"""
QUESTION:
Write a function `match_two_a` that takes a string as input and returns a boolean indicating whether the string contains exactly two 'a' characters, with any number of other characters before, between, and after the 'a' characters.
"""

import re

def match_two_a(s):
    """
    Returns True if the input string contains exactly two 'a' characters, 
    with any number of other characters before, between, and after the 'a' characters.

    Args:
        s (str): The input string.

    Returns:
        bool: Whether the string contains exactly two 'a' characters.
    """
    return bool(re.fullmatch(r'\b([^a]*a[^a]*){2}[^a]*\b', s))