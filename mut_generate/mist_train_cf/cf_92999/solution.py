"""
QUESTION:
Write a function `is_palindrome(s)` that checks whether a given string is a palindrome, ignoring any spaces and punctuation marks in the string. The function should be case-insensitive and return `True` if the string is a palindrome, `False` otherwise.
"""

import string

def entance(s):
    # Remove spaces and punctuation marks from the string
    s = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "")
    
    # Convert the string to lowercase
    s = s.lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]