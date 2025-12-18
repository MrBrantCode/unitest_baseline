"""
QUESTION:
Implement a function `count_word_frequency(string)` that takes a string as input, normalizes it to lowercase, removes all punctuation marks, splits it into words, and returns a dictionary where the keys are the words and the values are their frequencies. The function should exclude the words "and", "the", and "is" from the resulting dictionary.
"""

import re

def count_word_frequency(string):
    # Normalize string
    string = string.lower()
    string = re.sub(r'[^\w\s]', '', string)
    
    # Define stop words
    stop_words = ['and', 'the', 'is']
    
    # Split string into words
    words = string.split()
    
    # Count word frequency
    frequency = {}
    for word in words:
        if word not in stop_words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    
    return frequency