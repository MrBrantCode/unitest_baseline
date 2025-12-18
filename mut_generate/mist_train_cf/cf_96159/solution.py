"""
QUESTION:
Create a function `is_palindrome` that determines whether a given string is a palindrome, ignoring special characters, whitespace, numbers, and case sensitivity.
"""

import re

def is_palindrome(s):
    cleaned_string = re.sub('[^A-Za-z]', '', s.lower())
    return cleaned_string == cleaned_string[::-1]