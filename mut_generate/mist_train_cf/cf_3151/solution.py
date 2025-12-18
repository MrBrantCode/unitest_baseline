"""
QUESTION:
Implement a function `to_lowercase(s)` that takes a string `s` as input and returns the string in all lowercase. You are not allowed to use any built-in string manipulation functions or methods such as `toLowerCase()`, `lower()`, or any similar ones. Your algorithm must have a time complexity of O(n), where n is the length of the input string, and should implement a purely functional approach without using iteration or recursion.
"""

def to_lowercase(s):
    return ''.join(map(lambda c: chr(ord(c) + 32) if 'A' <= c <= 'Z' else c, s))