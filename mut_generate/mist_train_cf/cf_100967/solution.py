"""
QUESTION:
Write a function called `find_strings_with_two_identical_substrings` that takes a list of strings as input and returns the strings that contain exactly two identical substrings within them. The function should use regular expressions to match the substrings, and the substrings can be separated by any number of characters. Assume that the substrings are words (one or more word characters) and should be matched in a case-sensitive manner.
"""

import re

def find_strings_with_two_identical_substrings(strings):
    """
    Returns the strings that contain exactly two identical substrings within them.
    
    Args:
    strings (list): A list of strings.
    
    Returns:
    list: A list of strings that contain exactly two identical substrings.
    """
    pattern = r"\b(\w+)\b(.*\b\1\b){1,}"
    result = []
    for string in strings:
        if re.fullmatch(pattern, string):
            result.append(string)
    return result