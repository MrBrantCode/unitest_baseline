"""
QUESTION:
Create a function named `calculate_frequency` that calculates the frequency of unique case-sensitive alphabetic characters in a given sentence. The function should take a string as input, filter out non-alphabetic characters, and return a dictionary where keys are characters and values are their frequencies.
"""

from collections import Counter

def calculate_frequency(sentence):
    # Filter out the non-alphabetic characters from the sentence
    sentence = ''.join(c for c in sentence if c.isalpha())
    
    # Count the frequency of each character (case-sensitive)
    frequency = Counter(sentence)
    
    # Return the frequency dictionary
    return frequency