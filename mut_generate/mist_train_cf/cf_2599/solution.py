"""
QUESTION:
Write a function called `remove_whitespace` that takes a string as input and returns a string with the following modifications: 
- All leading and trailing whitespaces removed.
- All leading and trailing special characters removed.
- All consecutive whitespace characters replaced with a single space.
- The function should handle multiple consecutive whitespace characters between words.
- The function should be able to handle any type of input string.
"""

import re

def remove_whitespace(string):
    # Remove leading and trailing special characters
    string = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', string)
    
    # Remove leading and trailing whitespaces
    string = string.strip()
    
    # Replace consecutive whitespace characters with a single space
    string = re.sub(r'\s+', ' ', string)
    
    return string