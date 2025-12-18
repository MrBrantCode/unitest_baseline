"""
QUESTION:
Create a function `count_words` that takes a string `text` as input and returns the total number of words in the text. The function should exclude any punctuation marks, special characters, numbers, and alphanumeric characters that are not part of a word. The input text may contain multiple paragraphs.
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