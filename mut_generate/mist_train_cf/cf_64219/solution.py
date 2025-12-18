"""
QUESTION:
Create a function called `is_palindrome` that takes a string `s` as input and returns `True` if the string is a palindrome and `False` otherwise. The function should perform a case insensitive check, ignoring punctuation, whitespace, and special characters.
"""

import string

def is_palindrome(s):
    # Remove all punctuation and whitespace characters, and convert to lowercase.
    s = [char.lower() for char in s if char.isalnum()]
    
    # Compare the list with its reverse.
    return s == s[::-1]