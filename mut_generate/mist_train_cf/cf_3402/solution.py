"""
QUESTION:
Create a function `word_frequency(paragraph)` that takes a paragraph as input, ignores punctuation marks, considers words with different letter casing as the same word, excludes common words such as articles, prepositions, and conjunctions, and returns a dictionary of each unique word and its frequency in the paragraph. The function should handle paragraphs containing multiple sentences.
"""

import re
from collections import Counter

def word_frequency(paragraph):
    # Remove punctuation marks and convert to lowercase
    cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph.lower())
    
    # Split the paragraph into words
    words = cleaned_paragraph.split()
    
    # List of common words to exclude
    common_words = ['the', 'a', 'an', 'and', 'in', 'on', 'at', 'to', 'of', 'is', 'are', 'was', 'were', 'not', 'so', 'after', 'all']
    
    # Remove common words from the list of words
    filtered_words = [word for word in words if word not in common_words]
    
    # Count the frequency of each unique word
    word_counts = Counter(filtered_words)
    
    return dict(word_counts)