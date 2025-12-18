"""
QUESTION:
Write a function `find_dog_sentences` that captures all sentences with the word "dog" followed by any number of non-alphabetical characters, except the letters "x" and "y". The pattern should avoid matching sentences where "dog" has any alphabetical suffix. The function should be case-insensitive and robust to anomalies like punctuations immediately following "dog". It should return a list of matched sentences.
"""

import re

def find_dog_sentences(text):
    pattern = r'\bdog\b[^a-zA-Zxy]*(?=[^a-zA-Z]|$)'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    sentences = [match.group() for match in matches]
    return sentences