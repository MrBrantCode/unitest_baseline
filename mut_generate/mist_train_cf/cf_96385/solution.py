"""
QUESTION:
Write a function named `extract_unique_words` that takes a string as input, extracts all the unique alphanumeric words while maintaining their order of first occurrence, and returns them as a list. The function should be case-insensitive and ignore punctuation marks.
"""

import re

def extract_unique_words(sentence):
    sentence = sentence.lower()
    words = re.findall(r'\b\w+\b', sentence)
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words