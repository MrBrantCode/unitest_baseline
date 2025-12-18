"""
QUESTION:
Create a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome, considering only alphanumeric characters and ignoring case sensitivity, and `False` otherwise. The input string may contain non-alphanumeric characters and varying case.
"""

import re

def is_palindrome(s):
    s = re.sub('[^a-zA-Z0-9]', '', s.lower())
    reversed_s = s[::-1]
    return s == reversed_s