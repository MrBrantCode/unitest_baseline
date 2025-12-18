"""
QUESTION:
Design a function named `is_palindrome` that takes a string of alphanumeric characters as input and returns `True` if the string is the same when its characters are reversed, ignoring case and non-alphanumeric characters, and `False` otherwise. The input string may contain spaces and special characters.
"""

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]