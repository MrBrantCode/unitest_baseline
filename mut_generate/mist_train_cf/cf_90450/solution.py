"""
QUESTION:
Write a function named `most_frequent_word` that takes a string as input, returns the most frequently occurring word with a length greater than three, ignores punctuation, and is case insensitive. The function should have a time complexity of O(n), where n is the length of the input string, and should be optimized for memory usage.
"""

import re

def most_frequent_word(string):
    # Remove punctuation using regular expressions
    string = re.sub(r'[^\w\s]', '', string)
    
    # Convert to lowercase and split into words
    words = string.lower().split()
    
    # Create a dictionary to store word counts
    word_count = {}
    
    # Iterate through words and update count
    for word in words:
        if len(word) > 3:  # Ignore words with length <= 3
            word_count[word] = word_count.get(word, 0) + 1
    
    # Find the word with maximum count
    max_count = 0
    most_frequent = None
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_frequent = word
    
    return most_frequent