"""
QUESTION:
Write a function `is_substring(string1, string2)` that checks if `string2` is a substring of `string1` in a case-insensitive manner. The function should return `True` if `string2` is a substring of `string1`, regardless of the case, and `False` otherwise.
"""

def is_substring(string1, string2):
    return string2.lower() in string1.lower()