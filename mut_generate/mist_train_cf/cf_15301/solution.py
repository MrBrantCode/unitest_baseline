"""
QUESTION:
Create a function named `word_frequency` that takes a string as input and returns a dictionary where the keys are the words in the string and the values are their corresponding frequencies. The function should ignore any words that are less than 3 characters long or that contain any non-alphabetical characters, and handle cases in a case-insensitive manner.
"""

import re

def word_frequency(string):
    words = re.findall(r'\b\w{3,}\b', string.lower())
    frequency = {}
    
    for word in words:
        cleaned_word = re.sub(r'[^a-z]', '', word)
        frequency[cleaned_word] = frequency.get(cleaned_word, 0) + 1
    
    return frequency