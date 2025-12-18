"""
QUESTION:
Implement a function `calculate_word_frequencies` that takes a list of tuples, where each tuple contains a string and an integer, representing a word and its frequency, respectively. The function should return a dictionary where the keys are the unique words from the input list and the values are the total frequencies of each word. If a word appears multiple times in the list, its frequency should be accumulated.

The input list is a list of tuples, where each tuple is of the form `(str, int)`. The function should return a dictionary of the form `{str: int}`.
"""

from typing import List, Tuple, Dict

def calculate_word_frequencies(word_tuples: List[Tuple[str, int]]) -> Dict[str, int]:
    word_freq_dict = {}
    for word, freq in word_tuples:
        if word in word_freq_dict:
            word_freq_dict[word] += freq
        else:
            word_freq_dict[word] = freq
    return word_freq_dict