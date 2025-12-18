"""
QUESTION:
Write a function `isPalindrome` that checks if a given string is a palindrome, ignoring non-alphanumeric characters and considering the string case-insensitive. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

import re

def isPalindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub('[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the string is a palindrome
    return s == s[::-1]