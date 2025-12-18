"""
QUESTION:
Implement a function `count_distinct_words(text)` that takes a string of text as input and returns the count of distinct words, ignoring case sensitivity and common stop words. The function should split the input string into individual words using whitespace, punctuation marks, and special characters as delimiters, and then exclude common stop words from the count. The function must have a time complexity of O(n), where n is the length of the input string, and handle large input strings efficiently without consuming excessive memory.
"""

import re

def count_distinct_words(text):
    # Initialize a set to store the unique words encountered
    unique_words = set()
    
    # Split the input string into individual words using whitespace, punctuation marks, and special characters as delimiters
    words = re.findall(r'\w+', text.lower())
    
    # Remove common stop words from the count of distinct words
    stop_words = {'a', 'an', 'the'}
    words = [word for word in words if word not in stop_words]
    
    # Iterate through each word in the split result
    for word in words:
        # Add the word to the set (case-insensitive)
        unique_words.add(word)
    
    # Return the count of unique words stored in the set
    return len(unique_words)