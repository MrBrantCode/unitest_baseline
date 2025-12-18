"""
QUESTION:
Create a function `convert_to_uppercase(s)` that takes a string `s` containing only alphabetic characters as input and returns the string with all lowercase letters converted to uppercase without using the built-in `upper()` method or any loops.
"""

def convert_to_uppercase(s):
    return ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in s)