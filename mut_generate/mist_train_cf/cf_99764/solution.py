"""
QUESTION:
Create a function named `is_palindrome` that takes an input string and returns `True` if the string is a palindrome (reads the same forward and backward, ignoring non-alphanumeric characters and case) and `False` otherwise. The function should only consider alphanumeric characters and be case-insensitive.
"""

import re
def is_palindrome(s):
    s = re.sub(r'\W+', '', s).lower()
    return s == s[::-1]