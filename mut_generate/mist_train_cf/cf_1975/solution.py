"""
QUESTION:
Create a function named `remove_punctuation` that takes a string as input and returns a copy of the string with all punctuation marks and special characters removed, where punctuation marks include any characters that are not letters, numbers, or whitespace characters, and non-ASCII characters are preserved. The function should handle edge cases such as empty strings or strings that contain only punctuation marks.
"""

import re

def remove_punctuation(string):
    if not string:
        return ""
    
    # Use regular expression to remove punctuation marks and special characters
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    
    return cleaned_string