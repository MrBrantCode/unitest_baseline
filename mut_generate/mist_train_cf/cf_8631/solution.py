"""
QUESTION:
Write a function called `extract_words` that takes a sentence as input and returns a list of words between non-alphanumeric delimiters (excluding punctuation marks) that contain only letters and hyphens.
"""

import re

def extract_words(sentence):
    # Define the pattern for the delimiters
    delimiter_pattern = r'[^a-zA-Z0-9-]+'
    
    # Split the sentence by the delimiters
    words = re.split(delimiter_pattern, sentence)
    
    # Filter out the words that contain numbers or special characters other than hyphens
    filtered_words = [word for word in words if re.match(r'^[a-zA-Z-]+$', word)]
    
    return filtered_words