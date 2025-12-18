"""
QUESTION:
Write a function named `count_alphanumeric` that takes a string as input, extracts all alphanumeric characters while ignoring non-alphanumeric characters and case sensitivity, and returns a dictionary containing the frequency of each alphanumeric character.
"""

import collections

def count_alphanumeric(sentence):
    # Remove non-alphanumeric characters
    sentence = ''.join(e for e in sentence if e.isalnum())
    
    # Convert sentence to lowercase, as we have to ignore case sensitivity
    sentence = sentence.lower()

    # Use counter to count the frequencies of each alphanumeric character
    freq = collections.Counter(sentence)

    return freq