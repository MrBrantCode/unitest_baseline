"""
QUESTION:
Write a function named `is_palindrome` that determines if a given string is a palindrome, ignoring spaces, punctuation, and capitalization. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]