"""
QUESTION:
Write a function named `count_word_occurrences` that takes a string as input and returns the count of each unique word in the string, ignoring case sensitivity and punctuation. The function should consider sequences of characters separated by spaces as words and handle punctuation correctly.
"""

import re
from collections import defaultdict

def count_word_occurrences(input_string):
    # Remove punctuation and convert to lowercase
    input_string = input_string.lower()
    input_string = re.sub(r'[^\w\s]', '', input_string)
    
    # Split the string into words
    words = input_string.split()
    
    # Create a dictionary to store word counts
    word_counts = defaultdict(int)
    
    # Count occurrences of each word
    for word in words:
        word_counts[word] += 1
    
    return dict(word_counts)