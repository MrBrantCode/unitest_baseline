"""
QUESTION:
Write a function named `is_palindrome` that checks whether a given string is a palindrome or not. The function should be case-insensitive and ignore any non-alphanumeric characters. It should return `True` if the string is a palindrome and `False` otherwise. The function should also handle strings with leading/trailing spaces, multiple spaces between words, special characters, numbers, mix of uppercase/lowercase letters, and non-English characters. The time complexity of the function should be O(n), where n is the length of the string.
"""

import re

def is_palindrome(s):
    # Remove non-alphanumeric characters
    s = re.sub(r'\W+', '', s)
    
    # Convert to lowercase
    s = s.lower()
    
    # Check if the string is a palindrome
    return s == s[::-1]