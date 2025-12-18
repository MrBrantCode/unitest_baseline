"""
QUESTION:
Create a function named `count_word_occurrences(word, text)` that takes two parameters: `word` and `text`. This function should count the occurrences of `word` in `text`, excluding any occurrences within parentheses and ignoring punctuation marks, considering `word` as case insensitive.
"""

import re

def count_word_occurrences(word, text):
    # Remove punctuation marks from the text
    text = re.sub(r'[^\w\s]', '', text)

    # Remove text within parentheses
    text = re.sub(r'\([^)]*\)', '', text)

    # Create a regular expression pattern to match occurrences of the word
    pattern = rf'\b{word}\b'

    # Find all occurrences of the word in the text, excluding those within parentheses
    occurrences = re.findall(pattern, text, flags=re.IGNORECASE)

    # Count the occurrences and return the count
    return len(occurrences)