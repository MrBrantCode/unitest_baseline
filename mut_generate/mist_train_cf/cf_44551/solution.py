"""
QUESTION:
Write a function `replace_punctuation_with_ascii` that takes a string `s` as input and returns a new string where all non-alphanumeric characters (i.e., punctuation marks) have been replaced with their corresponding ASCII values. The function should not use excessive built-in functions and should handle strings containing alphanumeric characters, punctuation marks, and spaces.
"""

def replace_punctuation_with_ascii(s):
    return ''.join((str(ord(c)) if c.isalnum() is False else c) for c in s)