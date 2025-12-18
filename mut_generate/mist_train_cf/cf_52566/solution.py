"""
QUESTION:
Create a function named `is_palindrome` that takes a string `s` as input. The function should determine whether the string is a palindrome (reads the same forwards as backwards) considering case sensitivity, whitespace, punctuation, and numbers. It should return a boolean value where `True` indicates the string is a palindrome and `False` otherwise.
"""

import re

def is_palindrome(s: str) -> bool:
    cleaned_s = re.sub(r'\W+', '', s).lower()
    return cleaned_s == cleaned_s[::-1]