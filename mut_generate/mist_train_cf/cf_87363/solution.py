"""
QUESTION:
Construct a function `count_words` that takes a string of multiple sentences as input, ignores case sensitivity and punctuation marks, excludes any words that are palindromes and have an odd number of letters, and returns a dictionary of words with their corresponding counts if the count is greater than or equal to 3.
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
    return {word: count for word, count in word_counts.items() if count >= 3}