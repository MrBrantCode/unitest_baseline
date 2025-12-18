"""
QUESTION:
Create a function `is_palindrome` that takes two strings `str_1` and `str_2` as arguments. The function should return `True` if either `str_1` or `str_2` is a palindrome and `False` otherwise. A palindrome is a string that reads the same forward and backward, ignoring non-alphabetic characters and case. The function should return `False` if either `str_1` or `str_2` is `None` or empty.
"""

import re

def is_palindrome(str_1, str_2):
    if not str_1 or not str_2:
        return False
    
    str_1 = re.sub(r'[^a-zA-Z]', '', str_1.lower())
    str_2 = re.sub(r'[^a-zA-Z]', '', str_2.lower())
    
    return str_1 == str_1[::-1] or str_2 == str_2[::-1]