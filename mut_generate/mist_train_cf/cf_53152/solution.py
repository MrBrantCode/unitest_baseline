"""
QUESTION:
Construct a function `find_substrings` that takes a string as input and returns all substrings that start with 'a', end with 'Z', and contain at least one digit and one additional lowercase letter between 'a' and 'Z'. The function should be efficient enough to handle large strings composed of billions of characters.
"""

import re

def find_substrings(string):
    """
    This function takes a string as input and returns all substrings 
    that start with 'a', end with 'Z', and contain at least one digit 
    and one additional lowercase letter between 'a' and 'Z'.

    Args:
    string (str): The input string.

    Returns:
    list: A list of substrings that match the given pattern.
    """
    pattern = re.compile('a[a-z]*[0-9]+[a-z]+Z')
    results = pattern.findall(string)
    return results