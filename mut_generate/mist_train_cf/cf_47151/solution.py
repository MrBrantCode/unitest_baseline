"""
QUESTION:
Create a function `word_frequency` that takes a string `S` and a list of stop words as input. The function should return a dictionary containing the frequency of each word in the string, ignoring punctuation and case-sensitivity, and excluding the given stop words. The function should not include words that appear in the stop words list in the output dictionary.
"""

import string
from collections import Counter

def word_frequency(S, stop_words):
    """
    Calculate the frequency of each word in a string, ignoring punctuation and case-sensitivity,
    and excluding the given stop words.

    Args:
        S (str): The input string.
        stop_words (list): A list of stop words to be ignored.

    Returns:
        dict: A dictionary containing the frequency of each word in the string.
    """

    # Remove punctuation from the string and convert to lower case
    S = S.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the string into words
    words = S.split()

    # Filter out stop words and count the frequency of each word
    word_freq = Counter(word for word in words if word not in stop_words)

    return word_freq