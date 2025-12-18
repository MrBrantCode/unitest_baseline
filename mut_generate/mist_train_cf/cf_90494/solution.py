"""
QUESTION:
Create a function called "trimString" that takes a string as input and returns the string with leading and trailing whitespace characters removed and consecutive whitespace characters replaced with a single space. Preserve punctuation marks and special characters in the output string.
"""

import re

def trimString(string):
    # Remove leading and trailing whitespace characters
    trimmed_string = string.strip()
    
    # Remove consecutive whitespace characters
    trimmed_string = re.sub('\s+', ' ', trimmed_string)
    
    return trimmed_string