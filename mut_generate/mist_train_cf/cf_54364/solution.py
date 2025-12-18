"""
QUESTION:
Construct a function called `alphabetical_sort` that takes a string `text` as input, removes all non-alphabet characters, and returns the remaining characters in alphabetical order, with case-insensitive sorting.
"""

import re

def alphabetical_sort(text):
    # removing numbers and special symbols
    text_cleaned = re.sub('[^A-Za-z]+', '', text)
    
    # sort the letters in alphabetical order
    sorted_text = sorted(text_cleaned, key = lambda x: (x.lower(), x))
    
    return ''.join(sorted_text)