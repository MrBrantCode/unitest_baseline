"""
QUESTION:
Create a function `is_palindrome(s)` that takes a string `s` as input and returns a boolean indicating whether the string is a palindrome, i.e., reads the same backward as forward. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
    """
    Returns True if the given string is a palindrome, False otherwise.
    """
    return s == s[::-1]