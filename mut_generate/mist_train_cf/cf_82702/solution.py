"""
QUESTION:
Create a function `word_frequency(text)` that takes a string as input, counts the frequency of each word, and returns a dictionary where the keys are the individual words (ignoring case sensitivity and punctuation) and the values are their respective frequencies.
"""

import string
from collections import Counter

def word_frequency(text):
    text = text.lower()
    # Remove punctuations
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return dict(Counter(words))