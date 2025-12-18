"""
QUESTION:
Create a function named `is_anagram` that takes two phrases as input and determines if they are anagrams, ignoring case differences, punctuation marks, and allowing anagrams of different lengths. The function should return True if the phrases are anagrams and False otherwise.
"""

import re

def is_anagram(phrase1, phrase2):
    # Remove punctuation marks and convert to lowercase
    phrase1 = re.sub(r'[^\w\s]', '', phrase1).lower()
    phrase2 = re.sub(r'[^\w\s]', '', phrase2).lower()

    # Count the frequency of each letter in both phrases
    freq1 = {}
    freq2 = {}

    for letter in phrase1:
        freq1[letter] = freq1.get(letter, 0) + 1

    for letter in phrase2:
        freq2[letter] = freq2.get(letter, 0) + 1

    # Check if the frequencies of all letters are the same
    return freq1 == freq2