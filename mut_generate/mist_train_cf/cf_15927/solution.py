"""
QUESTION:
Create a function `is_palindrome(s)` that takes a string `s` as input and returns a boolean value. The function should check if the input string is a palindrome, ignoring non-alphanumeric characters, spaces, punctuation, and capitalization. It should treat uppercase and lowercase letters as equivalent and handle Unicode characters.
"""

import re

def is_palindrome(s):
    # Remove non-alphanumeric characters using regex
    s = re.sub('[\W_]', '', s)
    
    # Convert to lowercase
    s = s.lower()
    
    # Check if the reversed string is equal to the original string
    return s == s[::-1]