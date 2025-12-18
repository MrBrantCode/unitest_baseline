"""
QUESTION:
Write a function `extract_unique_words(paragraph)` that takes a string `paragraph` as input and returns a list of unique words in the order of their first occurrence, ignoring punctuation, special characters, and whitespace, and treating uppercase and lowercase letters as the same. The function should only consider alphanumeric characters as part of a word.
"""

import re

def extract_unique_words(paragraph):
    words = []
    seen_words = set()
    
    # Remove punctuation, special characters, and whitespace
    paragraph = re.sub(r'[^a-zA-Z0-9\s]', '', paragraph)
    
    # Split the paragraph into words
    for word in paragraph.split():
        # Convert the word to lowercase to make it case-insensitive
        word = word.lower()
        
        # Check if the word has already been seen
        if word not in seen_words:
            seen_words.add(word)
            words.append(word)
    
    return words