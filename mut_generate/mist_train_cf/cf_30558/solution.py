"""
QUESTION:
Create a function named `word_frequency` that takes a string of text as input and returns the frequency of each word in the text. The function should be case-insensitive and ignore punctuation. The output should be a dictionary with words as keys and their frequencies as values, sorted in alphabetical order by word.
"""

import string
from collections import Counter

def word_frequency(text):
    # Remove punctuation and convert text to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    frequency = Counter(words)
    
    # Sort the dictionary by keys
    sorted_frequency = dict(sorted(frequency.items()))
    
    return sorted_frequency