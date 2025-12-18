"""
QUESTION:
Create a function `is_palindrome(s)` that determines whether a given string `s` is a palindrome or not. The function should ignore spaces, punctuation marks, and capitalization. It should return `True` if the string is a palindrome and `False` otherwise. The function should only consider alphanumeric characters and disregard any non-alphanumeric characters.
"""

import string

def is_palindrome(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())
    return s == s[::-1]