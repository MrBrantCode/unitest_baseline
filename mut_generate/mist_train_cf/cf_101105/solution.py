"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns `True` if the input string is a palindrome and `False` otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring non-alphanumeric characters and case differences.
"""

import re
def is_palindrome(s):
    s = re.sub(r'\W+', '', s).lower()
    return s == s[::-1]