"""
QUESTION:
Write a function `has_unique_characters(s)` that takes a string `s` as input and returns `True` if all characters in the string are unique and `False` otherwise. The function should consider punctuation marks and special characters as unique characters, but it should exclude any whitespace characters from the string.
"""

import string

def has_unique_characters(s):
    # Remove whitespace characters from the string
    s = "".join(c for c in s if c not in string.whitespace)
    
    # Check if the remaining characters are unique
    unique_chars = set(s)
    
    return len(s) == len(unique_chars)