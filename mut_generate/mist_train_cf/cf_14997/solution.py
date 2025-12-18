"""
QUESTION:
Write a function `match_hello_people` that takes a string as input and returns True if the string contains the phrase "hello people" exactly once, with the following conditions:
- The match is case-insensitive.
- The phrase is not preceded or followed by any word characters.
- The function should be optimized for performance.
"""

import re

def match_hello_people(s):
    """
    Returns True if the string contains the phrase "hello people" exactly once, 
    with the conditions that the match is case-insensitive and the phrase is not 
    preceded or followed by any word characters.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    bool: True if the string matches the conditions, False otherwise.
    """
    pattern = r'^(?i)(?<!\w)hello people(?!\w)$'
    return bool(re.fullmatch(pattern, s))