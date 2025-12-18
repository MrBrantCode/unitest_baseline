"""
QUESTION:
Create a function `validate_linguistic_unit` that takes a string as input and returns `True` if the string matches the following conditions and `False` otherwise: 
- The string is constructed exclusively from lowercase components of the English alphabet.
- The string has a minimum of 5 characters and a maximum of 15 characters.
- The string does not begin or end with vowels.
- The string does not contain the same character repeated consecutively more than twice.
"""

import re

def validate_linguistic_unit(s):
    """
    Validate if a string matches the conditions of a linguistic unit.
    
    The string is constructed exclusively from lowercase components of the English alphabet.
    The string has a minimum of 5 characters and a maximum of 15 characters.
    The string does not begin or end with vowels.
    The string does not contain the same character repeated consecutively more than twice.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string matches the conditions, False otherwise.
    """
    pattern = r'^[^aeiou](?!.*([a-z])\1\1)[a-z]{3,13}[^aeiou]$'
    return bool(re.fullmatch(pattern, s))