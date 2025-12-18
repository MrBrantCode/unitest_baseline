"""
QUESTION:
Write a function `most_frequent_word` that takes a list of strings as input and returns the most frequently used word(s) in the list. The function should ignore case, punctuation, and special characters when counting word frequencies. If there are multiple words with the same highest frequency, the function should return all of them. The function should also handle cases where the input list is empty, contains only empty strings, contains only special characters or numbers, or contains non-string data types. If no valid words are found, the function should return an error message.
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