"""
QUESTION:
Write a function `convert_string(string)` that takes a string of uppercase and lowercase letters with possible punctuation marks as input. The function should return the input string with all punctuation marks removed and all words separated by a single underscore. If multiple consecutive spaces occur between words, they should be replaced with a single underscore.
"""

import re

def convert_string(string):
    # Remove all punctuation marks
    string = re.sub(r'[^\w\s]', '', string)
    
    # Replace multiple consecutive spaces with a single underscore
    string = re.sub(r'\s+', '_', string)
    
    # Replace remaining spaces with underscores
    string = string.replace(' ', '_')
    
    return string