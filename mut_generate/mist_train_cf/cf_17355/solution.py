"""
QUESTION:
Create a function called `count_words` that takes a string `text` as input and returns the total number of words in the text, excluding any punctuation marks, special characters, numbers, or alphanumeric characters that are not part of a word. The function should be able to handle large text inputs with multiple paragraphs.
"""

import re

def count_words(text):
    # Remove punctuation marks and special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Split the text into words
    words = text.split()

    # Count the number of words
    word_count = len(words)

    return word_count