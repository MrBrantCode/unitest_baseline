"""
QUESTION:
Write a function `is_palindrome(s)` that determines if a given string `s` is a palindrome, ignoring spaces and punctuation marks. The function should return `True` if `s` is a palindrome and `False` otherwise.
"""

import string
def entrance(s):
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "").lower()
    return s == s[::-1]