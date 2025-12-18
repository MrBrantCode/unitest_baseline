"""
QUESTION:
Write a function called `find_pattern` that uses regular expressions to find all occurrences of a given pattern in a string. The pattern must be preceded by the word "quick" and followed by a whitespace character. The function should return a list of all occurrences found.
"""

import re

def find_pattern(string, pattern):
    """
    Find all occurrences of a given pattern in a string, 
    preceded by the word "quick" and followed by a whitespace character.

    Args:
        string (str): The input string to search in.
        pattern (str): The pattern to search for.

    Returns:
        list: A list of all occurrences found.
    """
    return re.findall(rf'(?<=quick ){pattern}(?=\s)', string)