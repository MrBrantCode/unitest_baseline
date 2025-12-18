"""
QUESTION:
Write a function named `calculate_frequency` that takes an input dictionary of type `dict` where keys are words and values are their corresponding frequencies. The function should calculate the frequency of each word as a percentage of the total number of words, rounded to the nearest whole number, and print out the words in descending order of their frequency. If two or more words have the same frequency, sort them alphabetically. The function should handle input dictionaries with up to 1 million words efficiently.
"""

from typing import Dict
from math import isclose

def calculate_frequency(dictionary: Dict[str, int]) -> None:
    word_freq = {}
    for word in dictionary:
        word_freq[word] = word_freq.get(word, 0) + 1

    total_words = sum(word_freq.values())

    def custom_sort(item):
        word, freq = item
        return (-freq, word)

    sorted_words = sorted(word_freq.items(), key=custom_sort)

    for word, freq in sorted_words:
        percentage = round((freq / total_words) * 100)
        print(f"{word}: {percentage}%")