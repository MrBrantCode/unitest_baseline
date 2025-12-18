"""
QUESTION:
Create a function named `count_unique_words` that takes a sentence as input and returns the number of unique words in the sentence, excluding punctuation marks.
"""

import string

def count_unique_words(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    unique_words = set(words)
    return len(unique_words)