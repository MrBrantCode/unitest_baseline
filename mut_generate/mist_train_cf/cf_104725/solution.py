"""
QUESTION:
Create a function `extract_unique_words(sentence)` that takes a sentence as input, extracts unique alphanumeric words while maintaining their order of first occurrence, ignores punctuation marks, and treats uppercase and lowercase letters as the same. The function should return a list of unique words in lowercase.
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