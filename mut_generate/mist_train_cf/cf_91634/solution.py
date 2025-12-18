"""
QUESTION:
Write a function named `find_substring` that uses regular expressions to find a substring in a given string. The substring should match the pattern 'an example' if and only if it is both preceded by the word 'This' and followed by a number, without using lookaheads. The function should return the matched substring if found, or a message indicating that the substring was not found.
"""

import re

def find_substring(s):
    """
    Find the substring 'an example' in a given string if it is both preceded by 'This' and followed by a number.

    Args:
    s (str): The input string.

    Returns:
    str: The matched substring if found, or a message indicating that the substring was not found.
    """
    pattern = r'This.*an example \d+'
    match = re.search(pattern, s)
    if match:
        return match.group()
    else:
        return "Substring not found."