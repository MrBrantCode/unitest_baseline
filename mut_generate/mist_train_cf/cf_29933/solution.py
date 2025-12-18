"""
QUESTION:
Implement a function `word_frequency(text)` that takes a string of text as input and returns a list of unique words along with their frequencies, sorted in descending order based on frequency. A word is defined as a sequence of characters separated by spaces, punctuation marks should be ignored, and the comparison of words should be case-insensitive. The output should not include any common stop words such as "the", "and", "of", "in", etc.
"""

import re
from collections import Counter

def word_frequency(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split the text into words
    words = text.split()
    
    # Define common stop words
    stop_words = {'the', 'and', 'of', 'in', 'a', 'an', 'to', 'on', 'for', 'with', 'is', 'are', 'was', 'were'}
    
    # Count the frequency of each word, excluding stop words
    word_counts = Counter(word for word in words if word not in stop_words)
    
    # Sort the word frequencies in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_counts