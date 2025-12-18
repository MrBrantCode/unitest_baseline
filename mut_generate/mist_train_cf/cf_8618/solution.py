"""
QUESTION:
Implement a function called "trimString" that takes a single string as input and returns the string with leading and trailing whitespace characters removed, and any consecutive whitespace characters within the string replaced with a single space. The function should preserve punctuation marks and special characters.
"""

import re

def trimString(string):
    # Remove leading and trailing whitespace characters
    trimmed_string = string.strip()
    
    # Remove consecutive whitespace characters
    trimmed_string = re.sub('\s+', ' ', trimmed_string)
    
    return trimmed_string