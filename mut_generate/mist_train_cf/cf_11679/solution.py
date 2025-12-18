"""
QUESTION:
Create a function `is_palindrome(string)` that takes a string as input and returns `True` if it is a palindrome and `False` otherwise. The function should ignore spaces and punctuation marks, be case-insensitive, and handle edge cases where the input string is empty or contains only spaces.
"""

import re

def is_palindrome(string):
    # Remove spaces and punctuation marks, and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    
    # Compare the cleaned string with its reversed version
    return cleaned_string == cleaned_string[::-1]