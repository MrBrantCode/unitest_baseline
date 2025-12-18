"""
QUESTION:
Create a function `match_lowercase_word` that takes a string as input and returns True if the string is a single word that consists only of lowercase alphabets and has a length of at least 5 characters, and False otherwise.
"""

import re

def match_lowercase_word(s):
    """
    This function checks if the input string is a single word that consists only of lowercase alphabets and has a length of at least 5 characters.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    bool: True if the string is a single word that consists only of lowercase alphabets and has a length of at least 5 characters, False otherwise.
    """
    return bool(re.match('^[a-z]{5,}$', s))