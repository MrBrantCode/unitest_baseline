"""
QUESTION:
Write a function `parse_string(string)` that takes a string as input and returns a set of unique words. The string may contain punctuation marks and special characters. All punctuation marks and special characters should be removed, and the words should be case-insensitive (i.e., 'Word' and 'word' are considered the same word).
"""

import re

def parse_string(string):
    # Remove all punctuation marks and special characters
    string = re.sub(r'[^\w\s]', '', string)
    
    # Split the string into words
    words = string.split()
    
    # Convert the words into lowercase and create a set of unique words
    unique_words = set(word.lower() for word in words)
    
    return unique_words