"""
QUESTION:
Write a function called `tokenize` that takes a sentence as input, removes punctuation marks, splits the sentence into words, and removes common stop words ("the", "and", "is", "a", "I", "am", "an", "are", "it", "in", "to", "of") from the tokenized sentence. The function should return a list of words.
"""

import re

def tokenize(sentence):
    # Remove punctuation marks
    sentence = re.sub(r'[^\w\s]', '', sentence)
    
    # Tokenize sentence into words
    words = sentence.split()
    
    # Remove stop words
    stop_words = ['the', 'and', 'is', 'a', 'I', 'am', 'an', 'are', 'it', 'in', 'to', 'of']
    words = [word for word in words if word.lower() not in stop_words]
    
    return words