"""
QUESTION:
Implement a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if `s` is a palindrome (ignoring spaces, punctuation, and capitalization) and `False` otherwise.
"""

def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]