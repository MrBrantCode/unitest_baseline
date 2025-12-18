"""
QUESTION:
Create a function named `count_words` that takes two parameters: a string and an optional list of words to exclude. The function should count the occurrences of unique words in the string, excluding a predefined set of common words ("the", "a", "is", "and", "of", "in") and any additional words provided in the optional list. The function should return a dictionary-like object with the word counts, considering only lowercase words.
"""

import re
from collections import Counter

def count_words(string, exclude_words=[]):
    # Define common words to exclude
    common_words = set(['the', 'a', 'is', 'and', 'of', 'in'])
    
    # Exclude user-defined words from common words
    common_words = common_words.union(set(exclude_words))
    
    # Split string into words
    words = re.findall(r'\b\w+\b', string.lower())
    
    # Count the number of times each unique word is used, excluding common words
    word_count = Counter(word for word in words if word not in common_words)
    
    return word_count