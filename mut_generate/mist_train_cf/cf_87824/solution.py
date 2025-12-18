"""
QUESTION:
Implement a function `to_lowercase(s)` that converts a given string `s` to an all lowercase string without using any built-in string manipulation functions or methods. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any iteration or recursion.
"""

def to_lowercase(s):
    return ''.join(map(lambda c: chr(ord(c) + 32) if 'A' <= c <= 'Z' else c, s))