"""
QUESTION:
Write a function named `count_words` that takes a string `sentence` as input and returns the number of words in the sentence. The function should consider contractions (e.g., "don't") and hyphenated words (e.g., "well-known") as single entities.
"""

import re

def count_words(sentence):
    words = re.findall(r'\b\w[\w-]*\'*\w*\b', sentence)
    return len(words)