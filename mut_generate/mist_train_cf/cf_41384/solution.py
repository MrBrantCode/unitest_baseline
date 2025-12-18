"""
QUESTION:
Implement a function `word_count(text)` that takes a string of text as input and returns a dictionary containing the unique words as keys and their respective counts as values. The function should ignore punctuation marks and consider words in a case-insensitive manner, excluding common English stop words from the word count. The input text may contain punctuation marks, special characters, and stop words.
"""

import re
from collections import Counter

def word_count(text):
    # Convert text to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Define common English stop words
    stop_words = {'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'or', 'but', 'is', 'are', 'was', 'were'}
    
    # Split the text into words and count their occurrences
    words = text.split()
    word_counts = Counter(word for word in words if word not in stop_words)
    
    return dict(word_counts)