"""
QUESTION:
Write a function called `word_ratio` that takes a sentence as input and returns a dictionary with unique words as keys and their corresponding ratios to the total number of words as values. The function should ignore punctuation marks.
"""

import re
from collections import Counter

def word_ratio(sentence):
    # Remove punctuation marks and convert to lower case
    sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Calculate the total number of words
    total_words = len(words)
    
    # Calculate and return the ratio of each unique word
    return {word: count/total_words for word, count in word_count.items()}