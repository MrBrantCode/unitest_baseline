"""
QUESTION:
Write a function named `convert_string` that takes a string of uppercase and lowercase letters and punctuation marks as input, removes all punctuation marks, and replaces multiple consecutive spaces with a single underscore. The output should have all words separated by a single underscore.
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