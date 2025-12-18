"""
QUESTION:
Design a function `first_recurring_word` that takes a string `input_text` as input and returns the first recurring word and its index positions of the first and second occurrence. The function should be case-insensitive, ignore punctuation and numbers, and return "No recurring word found" if no recurring word is found.
"""

import re

def first_recurring_word(input_text):
    # Remove punctuation and numbers
    cleaned_text = re.sub(r'[^\w\s]','',input_text)
    cleaned_text = re.sub(r'\d+', '', cleaned_text)

    # Split the string into words
    words = cleaned_text.lower().split()

    # Create a dictionary to hold word counts
    word_counts = {}

    # Iterate over the list of words
    for i, word in enumerate(words):
        if word in word_counts:
            return word, word_counts[word], i
        else:
            word_counts[word] = i

    # If no recurring word is found, return an appropriate message
    return "No recurring word found"