"""
QUESTION:
Create a function `find_dog_sentences` that takes a list of sentences as input and returns a list of sentences containing the term "dog" followed by any series of characters, excluding the alphabetic characters "x" and "y". The function should be case-sensitive and use a regular expression pattern to match the sentences.
"""

import re

def find_dog_sentences(sentences):
    pattern = 'dog[^xy]*'
    return [sentence for sentence in sentences if re.search(pattern, sentence)]