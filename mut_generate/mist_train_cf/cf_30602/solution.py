"""
QUESTION:
Implement a function called `count_word_occurrences` that takes in two parameters: `word` and `word_list`. The function should be case-insensitive and return the total number of occurrences of the given word in the list of strings, including partial matches. The `word` parameter is a string and the `word_list` parameter is a list of strings. The function should return an integer.
"""

from typing import List
import re

def count_word_occurrences(word: str, word_list: List[str]) -> int:
    count = 0
    word = word.lower()
    for sentence in word_list:
        sentence = sentence.lower()
        count += len(re.findall(r'\b' + word + r'\b', sentence))
    return count