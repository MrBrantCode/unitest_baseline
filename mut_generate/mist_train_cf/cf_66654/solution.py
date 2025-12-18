"""
QUESTION:
Write a function `same_chars` that takes two string inputs `s1` and `s2` and returns `True` if they contain exactly the same types and number of characters, ignoring case differences and punctuation. The function should be case-insensitive and should ignore all non-alphanumeric characters.
"""

import re

def same_chars(s1, s2):
    # Removes all the special characters and convert to lower case
    s1 = re.sub(r'\W+', '', s1).lower()
    s2 = re.sub(r'\W+', '', s2).lower()

    # Sorts the strings and compare them
    return sorted(s1) == sorted(s2)