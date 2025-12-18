"""
QUESTION:
Write a Python function `filter_strings` that filters a list of strings. The function should return a list of strings that match the following conditions:
- The string starts with a letter.
- The string ends with a number.
- The string contains at least one uppercase letter and one lowercase letter.
- The string does not contain any special characters.
- The string does not contain any duplicate letters.

The function should take a list of strings as input and return a list of filtered strings.
"""

import re

def filter_strings(strings):
    """
    Filters a list of strings based on certain conditions.

    Args:
    strings (list): A list of strings to be filtered.

    Returns:
    list: A list of filtered strings.
    """
    pattern = r'^(?!.*(.).*\1)[A-Za-z][A-Za-z0-9]*[a-z][A-Za-z0-9]*[A-Z][A-Za-z0-9]*\d$'
    return [string for string in strings if re.match(pattern, string)]