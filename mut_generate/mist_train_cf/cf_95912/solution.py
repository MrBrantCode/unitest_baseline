"""
QUESTION:
Write a function named `match_strings` that takes two parameters, `string1` and `string2`, where `string2` contains a regular expression pattern. The function should return `True` if `string1` matches the pattern in `string2` and `False` otherwise. The time complexity of the function should be less than O(n^2) and the space complexity should be less than O(n), where n is the length of `string1`.
"""

import re

def match_strings(string1, string2):
    """
    This function checks if string1 matches the regular expression pattern in string2.

    Args:
        string1 (str): The string to be checked.
        string2 (str): The regular expression pattern.

    Returns:
        bool: True if string1 matches the pattern in string2, False otherwise.
    """
    return bool(re.match(string2, string1))