"""
QUESTION:
Write a function `isPalindrome(s)` that checks if a given string `s` is a palindrome, ignoring non-alphanumeric characters and being case insensitive. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

import re

def entrance(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub('[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the string is a palindrome
    return s == s[::-1]