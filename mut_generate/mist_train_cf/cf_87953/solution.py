"""
QUESTION:
Write a function `get_string_length(string)` that takes a string as input, removes punctuation marks, replaces multiple consecutive whitespace characters with a single whitespace, removes leading and trailing whitespaces, and returns the count of alphanumeric characters in the string. The function should handle uppercase and lowercase letters, digits, and special characters, and consider multiple consecutive whitespace characters as a single whitespace character.
"""

import re

def get_string_length(string):
    # Remove punctuation marks
    string = re.sub(r'[^\w\s]', '', string)
    
    # Replace multiple consecutive whitespaces with a single whitespace
    string = re.sub(r'\s+', ' ', string)
    
    # Remove leading and trailing whitespaces
    string = string.strip()
    
    # Count the alphanumeric characters
    count = sum(1 for char in string if char.isalnum())
    
    return count