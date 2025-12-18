"""
ORIGINAL QUESTION:
Create a function `word_frequency` that takes a string `text` as input and outputs the frequency of each word in the text. A word is defined as a sequence of alphanumeric characters separated by any non-alphanumeric character. The frequency count should be case-insensitive, ignoring punctuation and treating uppercase and lowercase letters as equivalent.
"""

import re

def word_frequency(text):
    text = text.lower()
    words = re.findall(r'\w+', text)
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency