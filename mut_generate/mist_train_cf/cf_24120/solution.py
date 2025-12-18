"""
QUESTION:
Write a function `normalize_string` that takes a string as input, converts it to lowercase, and removes all punctuation marks.
"""

import string

def normalize_string(s):
    """
    This function takes a string as input, converts it to lowercase, and removes all punctuation marks.

    Args:
        s (str): The input string.

    Returns:
        str: The normalized string.
    """
    s = s.lower()
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)