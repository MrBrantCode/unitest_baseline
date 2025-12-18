"""
QUESTION:
Write a function called `is_palindrome` that checks if a given input string is a palindrome. The function should be case-insensitive and ignore any punctuation marks and spaces. It should return `True` if the input string is a palindrome and `False` otherwise.
"""

import string

def is_palindrome(s):
    s = s.translate(str.maketrans("", "", string.punctuation + " ")).lower()
    return s == s[::-1]