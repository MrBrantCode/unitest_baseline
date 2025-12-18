"""
QUESTION:
Write a function named `remove_spaces_and_punctuation` that takes a string as input and returns the string with all blank spaces and punctuation marks removed.
"""

import re

def remove_spaces_and_punctuation(text):
    # Remove blank spaces
    text = re.sub(r'\s+', '', text)
    
    # Remove punctuation marks
    text = re.sub(r'[^\w\s]', '', text)
    
    return text