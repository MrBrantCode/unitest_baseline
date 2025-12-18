"""
QUESTION:
Create a function named `is_palindrome` that takes a string as input. The function should determine if the input string is a palindrome by ignoring special characters, whitespace, and punctuation, and considering the comparison case-insensitive. The function should return True if the input string is a palindrome and False otherwise.
"""

import re

def is_palindrome(input_string):
    # Remove special characters, whitespace, and punctuation
    cleaned_string = re.sub(r"[^a-zA-Z0-9]", "", input_string.lower())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]