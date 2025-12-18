"""
QUESTION:
Create a function called `count_words` that takes a string of words as input, counts the frequency of each word (ignoring case, punctuation marks, and special characters), and returns a dictionary with the word as the key and the frequency as the value. The function should treat words with different cases as the same word.
"""

import re

def count_words(word_string):
    """
    Counts the frequency of each word in a string, ignoring case, punctuation marks, and special characters.

    Args:
        word_string (str): The input string of words.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    word_string = word_string.lower()
    word_string = re.sub(r'[^\w\s]', '', word_string)
    words = word_string.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count