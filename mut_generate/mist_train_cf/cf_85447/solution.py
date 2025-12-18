"""
QUESTION:
Create a function `count_chars(s)` that takes a string `s` as input and returns a dictionary where the keys are the uppercase letters from the string and the values are the counts of each letter, ignoring special characters and whitespaces.
"""

import collections

def count_chars(s):
    s = ''.join(c for c in s if c.isalpha() and c.isupper())  # Filter out non-alphabetic characters and lowercase letters
    return dict(collections.Counter(s))  # Count occurrences of each character