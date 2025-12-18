"""
QUESTION:
Create a function named `word_count` that takes a string of words as input and returns a dictionary where the keys are the words and the values are the number of occurrences of each word. The function should be case-insensitive, ignore punctuation, and correctly handle special characters and words with apostrophes. The function should also be efficient enough to handle very large input strings.
"""

import re
from collections import Counter

def word_count(string):
    # Convert the string to lowercase and remove punctuation
    string = re.sub(r'[^\w\s]', '', string.lower())
    
    # Split the string into words
    words = string.split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    return dict(word_counts)