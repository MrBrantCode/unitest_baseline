"""
QUESTION:
Write a function `count_unique_words` that takes a string as input, and returns the count of unique words in the string, ignoring case sensitivity, excluding any words that are less than 3 characters long, and removing any special characters or numbers.
"""

import re

def count_unique_words(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Remove special characters and numbers
    string = re.sub(r'[^a-zA-Z ]', '', string)
    
    # Split the string into words
    words = string.split()
    
    # Count the unique words
    unique_words = set()
    for word in words:
        # Exclude words that are less than 3 characters long
        if len(word) >= 3:
            unique_words.add(word)
    
    return len(unique_words)