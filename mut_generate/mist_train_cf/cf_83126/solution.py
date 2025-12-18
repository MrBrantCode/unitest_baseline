"""
QUESTION:
Write a function named `count_word_frequency` that takes a string as input, calculates the frequency of each word in the string while ignoring case sensitivity and punctuation, and returns a dictionary where the keys are the unique words and the values are their corresponding frequencies. The function should be case-insensitive and should ignore any punctuation.
"""

import collections
import string

def count_word_frequency(text):
    """
    Calculate the frequency of each word in the input string while ignoring case sensitivity and punctuation.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary where the keys are the unique words and the values are their corresponding frequencies.
    """
    # remove punctuation and convert to lower case
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # split the text into individual words
    words = text.split()
    
    # count the frequency of each word
    word_counts = collections.Counter(words)
    
    return word_counts