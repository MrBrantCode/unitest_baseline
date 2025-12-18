"""
QUESTION:
Construct a function `count_words(string)` that takes a string of multiple sentences as input, ignores case sensitivity and punctuation marks, and returns a dictionary with words and their corresponding counts. The function should exclude any words that are palindromes and have an odd number of letters, and only include words with a count greater than or equal to 3.
"""

import re

def count_words(string):
    string = string.lower()
    string = re.sub(r'[^\w\s]', '', string)
    words = string.split()
    word_counts = {}

    for word in words:
        if word == word[::-1] and len(word) % 2 != 0:
            continue

        word_counts[word] = word_counts.get(word, 0) + 1

    word_counts = {word: count for word, count in word_counts.items() if count >= 3}
    return word_counts