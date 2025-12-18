"""
QUESTION:
Write a Python function `match_hello_world` that generates a regular expression to match strings with "Hello", followed by an optional comma and any number of spaces, followed by "World" and any punctuation mark. The match should be case-insensitive.
"""

import re

def match_hello_world(s):
    """
    Match strings with "Hello", followed by an optional comma and any number of spaces, 
    followed by "World" and any punctuation mark. The match is case-insensitive.

    Parameters:
    s (str): The string to be matched.

    Returns:
    bool: True if the string matches the pattern, False otherwise.
    """
    pattern = re.compile(r"^hello\s*,?\s*world[^\w\s]$", re.IGNORECASE)
    return bool(pattern.match(s))