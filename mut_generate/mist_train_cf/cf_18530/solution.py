"""
QUESTION:
Write a function `count_unique_words` that takes a sentence as input, calculates the total number of unique words excluding repeated words and words comprised of only digits, and returns the count. The function should be case-insensitive and should consider punctuation as word separators.
"""

import string

def count_unique_words(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    unique_words = set()
    for word in words:
        if word.isdigit():
            continue
        unique_words.add(word.lower())
    return len(unique_words)