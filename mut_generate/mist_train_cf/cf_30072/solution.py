"""
QUESTION:
Implement a function named `countUniqueWords` that takes a string `inputString` as its parameter and returns a dictionary where the keys are the unique words in the input string and the values are the counts of each word. The function should be case-insensitive, ignore punctuation, and exclude common English stop words.
"""

import re

def countUniqueWords(inputString):
    stop_words = {"the", "and", "but", "of", "in", "to", "a", "is", "it", "that", "as", "on", "with", "for", "at", "by", "this", "from", "or", "an", "be", "are"}
    word_counts = {}
    
    # Remove punctuation and convert to lowercase
    inputString = re.sub(r'[^\w\s]', '', inputString).lower()
    
    # Split the string into words
    words = inputString.split()
    
    # Count the unique words
    for word in words:
        if word not in stop_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    
    return word_counts