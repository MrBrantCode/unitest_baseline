"""
QUESTION:
Write a function `is_palindrome(string)` that determines whether a given string is a palindrome, ignoring special characters and whitespace. The function should take a string as input and return `True` if the string is a palindrome, and `False` otherwise. The function should be case-insensitive.
"""

import re

def is_palindrome(string):
    # Remove special characters and whitespace
    string = re.sub('[^A-Za-z0-9]+', '', string.lower())

    # Check if the string is equal to its reverse
    return string == string[::-1]