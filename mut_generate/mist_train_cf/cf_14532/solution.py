"""
QUESTION:
Write a function `replace_consecutive_whitespaces` that takes a string as input, removes leading and trailing whitespaces, and replaces all consecutive whitespaces with a single space.
"""

import re

def replace_consecutive_whitespaces(string):
    # Remove leading and trailing whitespaces
    string = string.strip()
    
    # Replace consecutive whitespaces with a single space
    string = re.sub('\s+', ' ', string)
    
    return string