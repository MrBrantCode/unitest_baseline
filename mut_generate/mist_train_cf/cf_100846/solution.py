"""
QUESTION:
Write a function named `negative_lookbehind_regex` that implements a negative lookbehind in RegEx to match a given pattern only if it is not immediately preceded by another specified pattern. The function should return the matched strings.
"""

import re

def negative_lookbehind_regex(text, pattern):
    """
    This function uses a negative lookbehind in RegEx to match a given pattern 
    only if it is not immediately preceded by another specified pattern.

    Parameters:
    text (str): The input text to search in.
    pattern (str): The pattern to match, including the negative lookbehind.

    Returns:
    list: A list of matched strings.
    """
    matches = re.findall(pattern, text)
    return matches