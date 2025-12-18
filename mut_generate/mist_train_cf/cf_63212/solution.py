"""
QUESTION:
Write a function using a third-party library to perform a regular expression match on a string in a J2ME application, considering the performance trade-off of using regular expressions. The function should take a regular expression pattern and a string as input, and return all matches found in the string.
"""

import re

def find_matches(pattern, string):
    """
    Perform a regular expression match on a string.

    Args:
        pattern (str): The regular expression pattern.
        string (str): The string to search for matches.

    Returns:
        list: A list of all matches found in the string.
    """
    return re.findall(pattern, string)