"""
QUESTION:
Write a function `convert_to_uppercase(s)` that takes a string `s` as input, where `s` only contains alphabetic characters, and returns the string `s` in all uppercase letters without using the built-in string method `upper()` or any loops.
"""

def convert_to_uppercase(s):
    return ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in s)