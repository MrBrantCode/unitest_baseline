"""
QUESTION:
Write a Python function named `to_uppercase` that takes a string `s` as input and returns the string with all letters converted to uppercase without using the built-in `upper()` function.
"""

def to_uppercase(s):
    uppercase_str = ""
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        uppercase_str += uppercase_char
    return uppercase_str