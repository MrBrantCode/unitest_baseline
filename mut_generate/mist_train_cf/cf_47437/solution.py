"""
QUESTION:
Write a function `reverse_and_count_words` that takes a sentence as input and performs the following operations:

- Reverses the order of words in the sentence without reversing the letters of each word.
- Counts the frequency of each word, disregarding case sensitivity.

Restrictions: 
- The function should be case insensitive when counting word frequencies.
- The function should not reverse the letters of each word.
"""

import collections

def reverse_and_count_words(sentence):
    """
    Reverses the order of words in a sentence and counts the frequency of each word.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: A tuple containing the reversed words and a dictionary of word frequencies.
    """
    words = sentence.lower().split()
    reverse_words = " ".join(words[::-1])
    word_count = collections.Counter(words)
    return reverse_words, word_count