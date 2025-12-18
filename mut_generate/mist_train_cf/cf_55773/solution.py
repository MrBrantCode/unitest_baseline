"""
QUESTION:
Write a function named `count_triad_frequency` that takes two parameters: `text` (a paragraph of text) and `triad` (a string of three words). The function should count the frequency of the given triad in the text, ignoring case and punctuation. The function should return the total count of the triad in the text.
"""

import re

def count_triad_frequency(text, triad):
    text = re.sub(r'[^\w\s]', '', text).lower().split()
    triad = triad.lower().split()
    triad_frequency = 0

    for i in range(len(text) - 2):
        if text[i:i+3] == triad:
            triad_frequency += 1

    return triad_frequency