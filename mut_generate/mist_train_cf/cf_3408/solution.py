"""
QUESTION:
Write a function `get_string_length` that takes a string as input and returns the number of alphanumeric characters in the string, excluding any whitespace characters and punctuation marks.
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