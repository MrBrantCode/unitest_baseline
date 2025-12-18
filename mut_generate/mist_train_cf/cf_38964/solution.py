"""
QUESTION:
Write a function `countWordOccurrences(text: str, words: List[str]) -> Dict[str, int]` that takes a string `text` and a list of strings `words` as input. The function should return a dictionary where the keys are the words from the `words` list and the values are the number of times each word appears in the `text`. The function should perform case-insensitive word matching.
"""

from typing import List, Dict

def count_word_occurrences(text: str, words: List[str]) -> Dict[str, int]:
    word_counts = {}
    text = text.lower()  # Convert the text to lowercase for case-insensitive comparison
    words = [word.lower() for word in words]  # Convert the words to lowercase for case-insensitive comparison

    # Split the text into words and count occurrences
    for word in text.split():
        if word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts