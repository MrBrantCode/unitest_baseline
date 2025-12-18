"""
QUESTION:
Write a function `check_string_pattern` that takes a string as input and returns True if the string starts with a vowel, followed by at least one consonant, then a digit, and ends with a special character, and False otherwise.
"""

import re

def check_string_pattern(s):
    """
    Checks if a string starts with a vowel, followed by at least one consonant, 
    then a digit, and ends with a special character.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    pattern = r"^(a|e|i|o|u)[bcdfghjklmnpqrstvwxyz]+\d+[^a-zA-Z0-9\s]$"
    return bool(re.match(pattern, s, re.IGNORECASE))