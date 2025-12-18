"""
QUESTION:
Create a function named `is_palindrome(s)` that checks if a given string is a palindrome. The function should be case-insensitive and ignore non-alphanumeric characters. It should handle strings with leading/trailing spaces, multiple spaces, special characters, numbers, and non-English characters correctly. The function should return `True` if the string is a palindrome and `False` otherwise, and it should have a time complexity of O(n), where n is the length of the string.
"""

import re

def is_palindrome(s):
    # Remove non-alphanumeric characters
    s = re.sub(r'\W+', '', s)
    
    # Convert to lowercase
    s = s.lower()
    
    # Check if the string is a palindrome
    return s == s[::-1]