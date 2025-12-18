"""
QUESTION:
Design a function named `get_unique_words` that takes a string `sentence` as input, removes punctuation marks, converts the sentence to lowercase, splits it into words, and returns a list of unique words in no particular order. The function should ignore case sensitivity and not contain any duplicate words.
"""

import re

def get_unique_words(sentence):
    # Remove punctuation marks and convert the sentence to lowercase
    sentence = re.sub(r'[^\w\s]', '', sentence.lower())
    
    # Split the sentence into words
    words = sentence.split()
    
    # Create a set to store unique words
    unique_words = set()
    
    # Iterate through each word
    for word in words:
        unique_words.add(word)
    
    # Convert the set to a list and return it
    return list(unique_words)