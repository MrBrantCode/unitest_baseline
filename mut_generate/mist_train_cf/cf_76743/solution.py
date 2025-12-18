"""
QUESTION:
Create a function `is_palindrome(s)` that takes a string of ASCII alphanumeric characters as input. The function should return `True` if the string is the same when its characters are reversed (ignoring case and non-alphanumeric characters), and `False` otherwise.
"""

def is_palindrome(s):
    s = ''.join(ch for ch in s if ch.isalnum()).lower()
    return s == s[::-1]