"""
QUESTION:
Create a function `longest_word(sentence)` that takes a string `sentence` as input and returns the longest word that starts with a capital letter and contains at least one vowel, excluding any punctuation marks. The function should ignore case when checking for vowels.
"""

import re

def longest_word(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    words = sentence.split()
    longest = ""
    length = 0
    for word in words:
        if word[0].isupper() and re.search(r'[aeiou]', word, re.IGNORECASE):
            if len(word) > length:
                longest = word
                length = len(word)
    return longest