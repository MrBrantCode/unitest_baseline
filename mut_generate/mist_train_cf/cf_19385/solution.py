"""
QUESTION:
Write a function named `most_frequent_word` that takes a list of strings as input and returns the most frequently used word(s) in the list, ignoring case, punctuation, and special characters. The function should handle empty lists, lists containing only empty strings or special characters, lists containing non-string data types, and cases where all words have the same frequency. If there are multiple most frequent words, return all of them. If the list is empty or contains no valid words, return an error message.
"""

import re
from collections import defaultdict

def most_frequent_word(words):
    if not words:
        return "Error: Empty list"

    word_count = defaultdict(int)
    max_frequency = 0

    for word in words:
        if not isinstance(word, str):
            return "Error: List contains non-string data types"
        word = re.sub(r'[^\w\s]', '', word).lower()
        if word != "":
            word_count[word] += 1
            max_frequency = max(max_frequency, word_count[word])

    if max_frequency == 0:
        return "Error: No valid words in the list"

    most_frequent_words = []
    for word, count in word_count.items():
        if count == max_frequency:
            most_frequent_words.append(word)

    return most_frequent_words