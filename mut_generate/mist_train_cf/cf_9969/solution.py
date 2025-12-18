"""
QUESTION:
Create a function `get_sorted_words` that takes a string as input, removes punctuation marks and special characters, converts the string to uppercase, splits it into a list of words, and returns the words in alphabetical order. The input string should have a minimum length of 10 characters.
"""

import re

def get_sorted_words(string):
    # Remove all punctuation marks and special characters
    string = re.sub(r'[^\w\s]', '', string)
    
    # Convert the string to uppercase and split it into a list of words
    words = string.upper().split()
    
    # Sort the words in alphabetical order
    sorted_words = sorted(words)
    
    return sorted_words