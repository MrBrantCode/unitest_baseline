"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters: `words` (an array of strings with length between 1 and 10^6) and `target_word` (a string with length between 1 and 100). The function should return the number of occurrences of `target_word` in `words`, considering case sensitivity, word boundaries, and ignoring special characters.
"""

import re

def count_occurrences(words, target_word):
    count = 0
    target_word = re.sub(r'\W+', '', target_word)
    for word in words:
        word = re.sub(r'\W+', '', word)
        if word == target_word:
            count += 1
    return count