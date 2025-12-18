"""
QUESTION:
Write a function `is_palindrome(string)` that determines whether a given string is a palindrome or not, considering only alphanumeric characters and ignoring case sensitivity. The function should ignore all non-alphanumeric characters and return `True` if the string is a palindrome, `False` otherwise.
"""

import re

def is_palindrome(string):
    # Convert to lowercase
    string = string.lower()
    
    # Remove non-alphanumeric characters
    string = re.sub('[^a-z0-9]', '', string)
    
    # Check if the resulting string is equal to its reverse
    return string == string[::-1]