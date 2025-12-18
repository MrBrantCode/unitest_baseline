"""
QUESTION:
Write a function `word_frequency(text: str) -> dict` that takes a string of text as input and returns a dictionary where the keys are the unique words and the values are their frequencies. The function should ignore punctuation, be case-insensitive, and treat words with apostrophes as a single word.
"""

import re

def word_frequency(text: str) -> dict:
    clean_text = re.sub(r'[^\w\s]', '', text).lower()
    words = clean_text.split()
    frequency = {}
    for word in words:
        word = word.replace("'", "")
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency