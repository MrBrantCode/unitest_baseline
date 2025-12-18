"""
QUESTION:
Create a function `is_palindrome(s)` that determines whether a given string `s` is a palindrome, disregarding spaces, punctuation, and capitalization. The function should return `True` if `s` is a palindrome and `False` otherwise.
"""

def entrance(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]