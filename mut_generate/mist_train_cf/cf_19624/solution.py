"""
QUESTION:
Write a function named `calculate_frequency` that takes a dictionary of strings as keys and integers as values. The function should calculate the frequency of each word (key) in the dictionary as a percentage of the total number of words, round the percentage to the nearest whole number, and print the words in descending order of their frequency. If two or more words have the same frequency, they should be sorted alphabetically. The function should be able to handle input dictionaries with up to 1 million words efficiently.
"""

from typing import Dict

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