"""
QUESTION:
Write a function `count_letters(sentence)` that takes a string `sentence` as input and returns a dictionary where keys are letters and values are their respective counts. The function should exclude numbers, special characters, and punctuation marks from the count, be case-insensitive, and not count spaces. The input sentence can contain multiple languages and may include characters from different character sets.
"""

import re

def count_letters(sentence):
    counts = {}
    sentence = re.sub('[^a-zA-Zа-яА-Я]', '', sentence)
    sentence = sentence.lower()
    for letter in sentence:
        if letter != ' ':
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    return counts