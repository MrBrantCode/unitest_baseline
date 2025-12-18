"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` is a palindrome. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def entrance(s):
    """
    Returns True if the given string is a palindrome, False otherwise.
    """
    return s == s[::-1]