"""
QUESTION:
Write a function `validate_string(s)` that takes a string `s` as input and returns `True` if all alphabetic characters in the string are unique and `False` otherwise. The function should be case-sensitive and consider non-alphabetic characters as part of the string.
"""

def validate_string(s):
    return len([char for char in s if char.isalpha()]) == len(set([char for char in s if char.isalpha()]))