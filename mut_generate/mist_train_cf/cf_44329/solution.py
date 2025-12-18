"""
QUESTION:
Given a list of lowercase words, write a function `sort_words_and_count_chars` that sorts the list in descending order of word frequency and then alphabetically in case of ties. The function should also calculate the frequency of individual letters in the sorted list and return both the sorted list and the character frequency count.
"""

from collections import Counter

def sort_words_and_count_chars(word_list):
    word_counts = Counter(word_list)
    sorted_words = sorted(word_list, key=lambda x: (-word_counts[x], x))
    char_counts = Counter(''.join(sorted_words))

    return sorted_words, char_counts