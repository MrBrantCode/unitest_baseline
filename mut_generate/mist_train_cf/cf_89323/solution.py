"""
QUESTION:
Write a function `count_distinct_words(sentence: str) -> int` that takes a string sentence as input, and returns the number of distinct words in the sentence, ignoring case sensitivity and excluding any punctuation marks. The function should also remove common English stop words from the sentence before counting the distinct words. The input sentence only contains letters, spaces, and punctuation marks.
"""

import string

def count_distinct_words(sentence: str) -> int:
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Remove punctuation marks from the sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    # Split the sentence into words
    words = sentence.split()

    # Create a set to store the distinct words
    distinct_words = set(words)

    # Define a list of common English stop words
    stop_words = ['the', 'a', 'an', 'and', 'in', 'on', 'is', 'are']

    # Remove stop words from the set
    distinct_words -= set(stop_words)

    # Return the number of distinct words
    return len(distinct_words)