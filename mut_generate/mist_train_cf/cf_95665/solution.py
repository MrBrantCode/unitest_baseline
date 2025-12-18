"""
QUESTION:
Create a function called `word_count` that takes a string of words as input and returns a dictionary containing the count of each word, excluding common English stop words. The function should ignore case sensitivity, handle punctuation marks and special characters properly, and be able to handle very large input strings efficiently.
"""

import re
from collections import Counter

def word_count(word_string):
    # Convert the string to lowercase and split it into words
    words = re.findall(r'\w+', word_string.lower())
    
    # Define a list of common English stop words
    stop_words = ['a', 'an', 'the', 'is', 'of', 'etc.']
    
    # Use Counter to count the occurrence of each word, excluding stop words
    word_counts = Counter(word for word in words if word not in stop_words)
    
    return word_counts