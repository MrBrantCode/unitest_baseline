"""
QUESTION:
Write a function named `long_lexeme_frequency` that takes a string of text as an argument and returns a dictionary where the keys are the unique words in the text that are longer than 7 characters, and the values are their corresponding frequencies.
"""

import re
from collections import Counter

def long_lexeme_frequency(text):
    # tokenize the text
    words = re.findall(r'\b\w+\b', text)
    
    # filter out words that are less than or equal to seven characters long
    long_words = [word for word in words if len(word) > 7]
    
    # compute the frequency of each long word
    frequency = Counter(long_words)
    
    # return the dictionary
    return dict(frequency)