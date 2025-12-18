"""
QUESTION:
Create a function `is_palindrome` that checks if a given string is the same when its characters are reversed. The function should take a string as an argument and return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
    """
    Returns True if the given string is a palindrome, False otherwise.
    """
    return s == s[::-1]