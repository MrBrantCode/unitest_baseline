"""
QUESTION:
Create a function `count_consonant_vowel_words(sentence)` that takes a string `sentence` as input and returns the number of words that start with a consonant and end with a vowel, and have a length of 10 characters or less.
"""

import re

def count_consonant_vowel_words(sentence):
    count = 0
    words = sentence.split()
    for word in words:
        if re.match(r'^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ].*[aeiouAEIOU]$', word) and len(word) <= 10:
            count += 1
    return count