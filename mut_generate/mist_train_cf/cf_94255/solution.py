"""
QUESTION:
Write a function `invert_case` that takes a string as input and returns a new string where the case of each character is inverted, without using any built-in functions or methods for case conversion. The function should be implemented in a single line using a lambda function.
"""

def invert_case(s):
    return ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in s])