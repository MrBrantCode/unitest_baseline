"""
QUESTION:
Create a function `is_palindrome(string)` that determines whether an input string is a palindrome or not. The function should ignore spaces and punctuation marks, be case-insensitive, handle edge cases with empty or single-space strings, and use efficient algorithms for performance.
"""

import re

def is_palindrome(string):
    # Remove spaces and punctuation marks, and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z]', '', string.lower())
    
    # Check if the cleaned string is empty or contains only spaces
    if cleaned_string.strip() == '':
        return False
    
    # Compare the cleaned string with its reversed version
    return cleaned_string == cleaned_string[::-1]