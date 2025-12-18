"""
QUESTION:
Write a function called `process_sentence` that takes a string sentence as input, removes any punctuation, converts it to lowercase, removes any duplicate words, and returns the unique words in alphabetical order as a single string with spaces separating the words.
"""

import string

def process_sentence(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = sentence.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    return " ".join(sorted_words)