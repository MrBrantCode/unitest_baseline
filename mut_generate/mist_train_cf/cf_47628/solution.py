"""
QUESTION:
Write a function named `is_palindrome` that takes a string `s` as input, removes non-alphanumeric characters, and converts it to lowercase. The function should return `True` if the resulting string is a palindrome and `False` otherwise, ignoring the original string's case, whitespace, and punctuation.
"""

def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]