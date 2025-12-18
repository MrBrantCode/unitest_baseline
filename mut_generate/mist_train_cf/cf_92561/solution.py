"""
QUESTION:
Create a function `is_palindrome` that determines whether a given string is a palindrome, ignoring special characters and whitespace. The function should take a string as input, return `True` if the string is a palindrome and `False` otherwise, and handle case insensitivity by treating uppercase and lowercase letters as the same.
"""

import re

def is_palindrome(string):
    string = re.sub('[^A-Za-z0-9]+', '', string.lower())
    return string == string[::-1]