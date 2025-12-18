"""
QUESTION:
Create a function called `calculate_word_frequency` that calculates the frequency of a specific word within a given text. The function should be case-insensitive and only count whole words. The input parameters are the word to be searched and the text to search in, both of which are strings. The function should return the total occurrences of the word in the text.
"""

import re

def calculate_word_frequency(word, text):
    word = word.lower()
    text = text.lower()

    # Use regex to find all occurrences of the word
    matched_words = re.findall(r'\b' + word + r'\b', text)
    return len(matched_words)