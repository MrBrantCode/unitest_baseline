"""
QUESTION:
Write a function `is_palindrome(s)` that checks if the input string `s` is a palindrome. The function should be case-insensitive and ignore non-alphanumeric characters. It should return a boolean value and have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

import re

def is_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()
    
    # Remove non-alphanumeric characters using regular expression
    s = re.sub(r'[^a-z0-9]', '', s)
    
    # Check if the string is a palindrome
    return s == s[::-1]