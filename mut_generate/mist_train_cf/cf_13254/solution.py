"""
QUESTION:
Write a function named `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome, ignoring spaces, punctuation, and capitalization, and `False` otherwise.
"""

import re

def is_palindrome(string):
    # Remove spaces, punctuation, and convert to lowercase
    cleaned_string = re.sub(r'[^A-Za-z0-9]', '', string.lower())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]