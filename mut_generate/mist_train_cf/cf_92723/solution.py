"""
QUESTION:
Create a function named `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome, ignoring spaces, punctuation, and capitalization, and `False` otherwise. The function should not include any error handling for non-string inputs.
"""

import re

def is_palindrome(s):
    cleaned_string = re.sub(r'[^A-Za-z0-9]', '', s.lower())
    return cleaned_string == cleaned_string[::-1]