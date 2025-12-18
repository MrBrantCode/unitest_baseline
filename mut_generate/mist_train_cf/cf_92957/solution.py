"""
QUESTION:
Write a function `reverse_string` that takes a string `s` as input and returns the string reversed using a recursive approach without utilizing any built-in string manipulation functions or data structures.
"""

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]