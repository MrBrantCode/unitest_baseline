"""
QUESTION:
Create a function `is_palindrome(s)` that takes a string `s` as input, determines if it's a palindrome while ignoring spaces and punctuation marks, and returns a boolean value. The function should be case-insensitive.
"""

import string
def is_palindrome(s):
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "").lower()
    return s == s[::-1]