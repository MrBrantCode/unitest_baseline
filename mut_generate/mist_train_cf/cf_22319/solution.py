"""
QUESTION:
Write a function `count_words_with_vowel_start_end(sentence)` that takes a sentence as input and returns the number of words that start and end with a vowel (both lowercase and uppercase), excluding any words that contain a vowel followed immediately by a consonant. The input sentence can be assumed to contain at least 15 words and each word will have a maximum length of 20 characters.
"""

import re

def count_words_with_vowel_start_end(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    count = 0
    for word in words:
        # Exclude words with a vowel followed immediately by a consonant
        if re.search(r'[aeiou][^aeiou]', word):
            continue
        # Check if the word starts and ends with a vowel
        if re.match(r'^[aeiou].*[aeiou]$', word):
            count += 1
    return count