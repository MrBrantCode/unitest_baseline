"""
QUESTION:
Implement a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome (ignoring case, whitespace, punctuation, and special characters) and `False` otherwise.
"""

import re

def is_palindrome(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    
    return s == s[::-1]