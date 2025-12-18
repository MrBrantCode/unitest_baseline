"""
QUESTION:
Write a function `parse_string` that takes a string as input, removes any non-alphabetic characters and converts it to lowercase, then splits it into words. The function should handle multiple spaces between words and return an empty list if the input string is empty or consists only of non-alphabetic characters.
"""

import re

def parse_string(string):
    # Remove punctuation marks
    string = re.sub(r'[^\w\s]', '', string)
    
    # Split the string into words
    words = re.split(r'\s+', string.lower())
    
    return words