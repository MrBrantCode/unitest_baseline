"""
QUESTION:
Write a function called `sort_words_with_punctuation` that takes a string as input, rearranges its words in alphabetical order while preserving their original punctuation, and returns the resulting string.
"""

import string

def sort_words_with_punctuation(sentence):
    # remove punctuation for sorting
    words = [(i.strip(string.punctuation), i) for i in sentence.split()]

    # sort words
    words.sort()

    # reconstruct sentence with punctuation
    sorted_sentence = ' '.join([i[1] for i in words])

    return sorted_sentence