"""
QUESTION:
Write a function called `count_unique_words` that takes a string as input, ignores case sensitivity, and returns the count of unique words that are 3 characters or longer and contain only letters.
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