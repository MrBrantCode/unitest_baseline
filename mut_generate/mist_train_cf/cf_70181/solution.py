"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome (reads the same backward as forward, ignoring case and whitespace) and `False` otherwise. The function should be case-insensitive and ignore all whitespace in the input string.
"""

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]