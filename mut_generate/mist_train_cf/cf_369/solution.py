"""
QUESTION:
Write a Python function named `count_letters` that takes a sentence as input and returns a dictionary with letter counts. The function should exclude numbers, special characters, punctuation marks, and spaces, and should be case-insensitive. It should correctly handle sentences containing multiple languages and Unicode characters, including emojis. The input sentence is guaranteed to be 1000 characters or less.
"""

import re

def count_letters(sentence):
    letter_count = {}
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.replace(' ', '').lower()
    for letter in sentence:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count