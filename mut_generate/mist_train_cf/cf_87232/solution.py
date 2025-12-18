"""
QUESTION:
Create a function named `remove_punctuation` that takes a string as input and returns a copy of the string with all punctuation marks and special characters removed, considering both ASCII and non-ASCII characters. The function should handle edge cases such as empty strings or strings that contain only punctuation marks, and it must use regular expressions for character removal.
"""

import re

def remove_punctuation(string):
    if not string:
        return ""
    
    # Use regular expression to remove punctuation marks and special characters
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    
    return cleaned_string