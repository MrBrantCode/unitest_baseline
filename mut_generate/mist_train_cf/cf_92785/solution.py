"""
QUESTION:
Write a function called `count_word_frequency` that takes a string as input, removes all non-alphanumeric characters, counts the occurrences of each word, and returns the word counts in descending order of frequency.
"""

import re
from collections import Counter

def count_word_frequency(text):
    # Remove all non-alphanumeric characters
    clean_text = re.sub(r'\W+', ' ', text)
    
    # Split the text into individual words
    words = clean_text.lower().split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Sort the word counts in descending order of frequency
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_counts