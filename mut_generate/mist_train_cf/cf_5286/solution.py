"""
QUESTION:
Create a function `count_words_exclude_letter(sentence, letter)` that takes a sentence and a letter as input. The function should count and return the distinct words in the sentence, excluding any words that contain the given letter (case insensitive) or are longer than 5 characters. The function should handle punctuation marks and special characters, and only count each word once regardless of its frequency in the sentence.
"""

import re

def count_words_exclude_letter(sentence, letter):
    """
    Count and return the distinct words in the sentence, excluding any words that contain the given letter (case insensitive) or are longer than 5 characters.

    Args:
        sentence (str): The input sentence.
        letter (str): The letter to exclude.

    Returns:
        int: The count of distinct words.
    """

    letter = letter.lower()
    sentence = re.sub(r'[^\w\s]', '', sentence)
    words = sentence.lower().split()
    word_count = set()

    for word in words:
        if letter not in word and len(word) <= 5:
            word_count.add(word)

    return len(word_count)