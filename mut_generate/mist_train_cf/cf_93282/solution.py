"""
QUESTION:
Develop a function named `replace_consecutive_whitespaces` that takes a string as input and returns the string after removing any leading or trailing whitespaces and replacing all consecutive whitespaces with a single space.
"""

import re

def replace_consecutive_whitespaces(string):
    # Remove leading and trailing whitespaces
    string = string.strip()
    
    # Replace consecutive whitespaces with a single space
    string = re.sub('\s+', ' ', string)
    
    return string