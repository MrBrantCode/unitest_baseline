"""
QUESTION:
Implement a function `word_frequency` that calculates the frequency of each word in a given text, ignoring case sensitivity and considering only alphanumeric characters as part of a word. Punctuation and special characters should be disregarded. 

The function should take a string `text` as input and return a dictionary where the keys are the unique words in the input text and the values are the frequencies of the corresponding words.
"""

import re

def word_frequency(text: str) -> dict:
    word_freq = {}
    words = re.findall(r'\b\w+\b', text.lower())
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq