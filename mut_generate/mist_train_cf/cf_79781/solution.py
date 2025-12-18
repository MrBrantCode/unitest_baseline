"""
QUESTION:
Write a Python function `find_canadian_postal_code` that takes a string `text` as input, and returns the first occurrence of a legitimate Canadian postal code in the format A1A 1A1, where A is a letter in the range A to Z (excluding D, F, I, O, Q, and U) and 1 is a digit from 0 to 9, with a space separating the third and fourth characters. The function should return None if no legitimate Canadian postal code is found.
"""

import re

def find_canadian_postal_code(text):
    """
    Finds the first occurrence of a legitimate Canadian postal code in the input string.
    
    Args:
        text (str): The input string to search for a Canadian postal code.
    
    Returns:
        str or None: The first legitimate Canadian postal code found, or None if no code is found.
    """
    pattern = r'[ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ] \d[ABCEGHJKLMNPRSTVWXYZ]\d'
    re_search = re.search(pattern, text, re.IGNORECASE)
    return re_search.group() if re_search else None