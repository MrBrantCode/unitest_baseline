"""
QUESTION:
Write a function named `count_distinct_words` that takes a string `text` as input and returns the count of distinct words in the string, where words are considered distinct regardless of case and punctuation. The function should have a time complexity of O(n), where n is the length of the input string.
"""

import re

def entance(text):
    # Initialize a set to store unique words
    unique_words = set()
    
    # Split the input string into individual words
    words = re.findall(r'\w+', text.lower())
    
    # Iterate through each word
    for word in words:
        # Add the word to the set if it's not already present
        unique_words.add(word)
    
    # Return the count of unique words
    return len(unique_words)