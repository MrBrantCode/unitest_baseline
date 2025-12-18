"""
QUESTION:
Create a function `is_palindrome(s)` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome, ignoring non-alphanumeric characters and considering the comparison case-insensitive. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]