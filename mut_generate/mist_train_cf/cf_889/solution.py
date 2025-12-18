"""
QUESTION:
Write a Python function named `count_unique_words` that takes a sentence as input, removes punctuation marks and special characters, and returns the count of unique words in the sentence in reverse alphabetical order. The function should be case-insensitive.
"""

import re

def count_unique_words(sentence):
    # Remove punctuation marks and special characters
    clean_sentence = re.sub(r'[^\w\s]', '', sentence)
    
    # Split the sentence into words
    words = clean_sentence.split()
    
    # Get unique words and their count
    unique_words = {}
    for word in words:
        word = word.lower()
        if word not in unique_words:
            unique_words[word] = 1
        else:
            unique_words[word] += 1
    
    # Sort unique words in reverse alphabetical order
    sorted_unique_words = sorted(unique_words.keys(), reverse=True)
    
    # Return the count of unique words
    return len(sorted_unique_words)