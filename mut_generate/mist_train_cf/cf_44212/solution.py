"""
QUESTION:
Write a function `is_palindrome` that takes a string `s` as input, and returns `True` if the string is a palindrome (i.e., reads the same forward and backward, ignoring spaces, punctuation, and capitalization) and `False` otherwise.
"""

def is_palindrome(s):
    """
    Returns True if the string is a palindrome, False otherwise.

    The function ignores spaces, punctuation, and capitalization.
    """
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]