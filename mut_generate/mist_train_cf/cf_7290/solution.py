"""
QUESTION:
Create a function `count_frequencies(sentence)` that generates a dictionary containing the frequencies of all English alphabets in the given sentence, ignoring case sensitivity and punctuation marks, while correctly handling words with accents and diacritics.
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