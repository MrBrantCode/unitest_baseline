"""
QUESTION:
Write a function called `has_unique_characters` that takes a string `s` as input and returns `True` if all characters in the string are unique and `False` otherwise. The function should exclude whitespace characters from consideration. All other characters, including punctuation marks and special characters, should be considered as unique characters.
"""

import string

def has_unique_characters(s):
    s = "".join(c for c in s if c not in string.whitespace)
    unique_chars = set(s)
    return len(s) == len(unique_chars)