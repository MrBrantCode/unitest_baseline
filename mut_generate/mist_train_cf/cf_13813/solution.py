"""
QUESTION:
Create a function named `remove_spaces_and_punctuation` that takes a string as input, removes all blank spaces and punctuation marks from the string, and returns the modified string. The function should not print the output; instead, it should return the modified string for further processing.
"""

import re

def remove_spaces_and_punctuation(text):
    # Remove blank spaces
    text = re.sub(r'\s+', '', text)
    
    # Remove punctuation marks
    text = re.sub(r'[^\w\s]', '', text)
    
    return text