"""
QUESTION:
Create a function called `process_sentence(sentence)` that takes a sentence as input and returns a string of unique words in alphabetical order, case-insensitive, without any punctuation marks.
"""

import string

def process_sentence(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Remove punctuation marks
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    # Split the sentence into words
    words = sentence.split()

    # Find the unique words
    unique_words = set(words)

    # Sort the unique words in alphabetical order
    sorted_words = sorted(unique_words)

    # Return the sorted words as a string
    return " ".join(sorted_words)