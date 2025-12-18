"""
QUESTION:
Update the Python function `regex = re.compile(pattern)` to match any line with at least two occurrences of the substring "ABC". The function should return True if a given string matches the condition and False otherwise. The function should be case sensitive and should not match any characters in addition to 'A', 'B', 'C' in the substring. 

Note that the substring "ABC" should appear at least two times in a line.
"""

import re

def has_at_least_two_abc(string):
    """
    Checks if a given string has at least two occurrences of the substring "ABC".
    
    Args:
        string (str): The input string to check.
    
    Returns:
        bool: True if the string has at least two "ABC" substrings, False otherwise.
    """
    pattern = r"(.*ABC){2,}.*"
    regex = re.compile(pattern)
    return bool(regex.search(string))