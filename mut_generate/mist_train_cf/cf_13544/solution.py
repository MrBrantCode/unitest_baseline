"""
QUESTION:
Design a function `match_az` that takes a string as input and returns True if the string starts with the letter "a", ends with the letter "z", and contains at least one digit in between. The function should return False otherwise.
"""

import re

def match_az(s):
    """
    This function checks if the input string starts with 'a', ends with 'z', and contains at least one digit in between.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string matches the criteria, False otherwise.
    """
    pattern = r'^a.*\d+.*z$'
    return bool(re.match(pattern, s))