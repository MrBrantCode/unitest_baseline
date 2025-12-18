"""
QUESTION:
Create a regular expression pattern to match a single word that meets the following conditions:

- The word must be in one of two formats: "XX-XXX-XXX" or "YY-YYYY-YYYY".
- The first two characters of the word must be uppercase letters.
- For the "XX-XXX-XXX" format, the next three characters must be lowercase letters, and the last three characters can be a mix of uppercase and lowercase letters.
- For the "YY-YYYY-YYYY" format, the next four characters must be lowercase letters, and the last four characters can be a mix of uppercase and lowercase letters.
- The word must not contain any digits or special characters.

Write a function named `match_word_pattern` that takes a string as input and returns `True` if the string matches the pattern, and `False` otherwise.
"""

import re

def match_word_pattern(word):
    """
    This function checks if the input string matches the pattern.
    The pattern is one of two formats: "XX-XXX-XXX" or "YY-YYYY-YYYY".
    The first two characters must be uppercase letters.
    For the "XX-XXX-XXX" format, the next three characters must be lowercase letters, 
    and the last three characters can be a mix of uppercase and lowercase letters.
    For the "YY-YYYY-YYYY" format, the next four characters must be lowercase letters, 
    and the last four characters can be a mix of uppercase and lowercase letters.
    The word must not contain any digits or special characters.

    Args:
        word (str): The input string to be checked.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    pattern1 = r'^[A-Z]{2}-[a-z]{3}-[A-Za-z]{3}$'
    pattern2 = r'^[A-Z]{2}-[a-z]{4}-[A-Za-z]{4}$'
    
    return bool(re.match(pattern1, word)) or bool(re.match(pattern2, word))