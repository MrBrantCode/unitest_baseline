"""
QUESTION:
Implement the `count_word_occurrences` function to count the occurrences of a specific word in a given text. The function should be case-insensitive and only consider whole words, ignoring any partial matches within other words. The function takes two parameters: `text` (the input text) and `word` (the word to be searched).
"""

import re

def count_word_occurrences(text, word):
    # Preprocess the text and word to ensure case-insensitive matching
    text = text.lower()
    word = word.lower()

    # Use regular expression to find whole word occurrences
    occurrences = re.findall(r'\b' + word + r'\b', text)

    return len(occurrences)