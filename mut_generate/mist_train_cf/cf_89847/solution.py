"""
QUESTION:
Create a function named `count_frequencies(sentence)` that takes a sentence as input, counts the frequencies of all English alphabets (both lowercase and uppercase), and returns a dictionary containing the frequency of each alphabet. The function should ignore punctuation marks and correctly handle words with accents and diacritics.
"""

import string

def count_frequencies(sentence):
    frequencies = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
    return frequencies