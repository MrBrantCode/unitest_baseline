"""
QUESTION:
Design a function `word_frequency` that takes a string of predominantly alphabets as input and returns a dictionary of unique words with their frequencies of occurrence in the string. The function should be case-insensitive, ignore punctuation, and identify the most frequent word(s) in the string.
"""

import re
from collections import Counter

def word_frequency(string):
    # Convert text into lower case and remove punctuation
    string = re.sub(r'[^\w\s]', '', string.lower())
    
    # Tokenize the string into words
    words = string.split()
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Identify the most common word(s)
    most_common_words = word_count.most_common(1)
    
    return word_count, most_common_words