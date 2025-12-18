"""
QUESTION:
Create a function named `is_palindrome` that takes a string `s` as input. The function should return `True` if `s` is a palindrome and `False` otherwise. A palindrome is a sequence of characters that reads the same forward and backward, disregarding spaces, punctuation, and capitalization. The function should ignore any non-alphanumeric characters and treat uppercase and lowercase letters as equivalent.
"""

import re

def is_palindrome(s):
    # Remove non-alphanumeric characters using regex
    s = re.sub('[\W_]', '', s)
    
    # Convert to lowercase
    s = s.lower()
    
    # Check if the reversed string is equal to the original string
    return s == s[::-1]