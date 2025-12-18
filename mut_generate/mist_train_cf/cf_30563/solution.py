"""
QUESTION:
Implement the `word_frequency` function, which takes a string `text` as input and returns a dictionary where the keys are unique words in the text and the values are the frequency of each word. The function should be case-insensitive and remove any punctuation marks, considering contractions as separate words (e.g., "can't" should be treated as "can" and "t").
"""

import re

def word_frequency(text):
    # Convert the text to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency