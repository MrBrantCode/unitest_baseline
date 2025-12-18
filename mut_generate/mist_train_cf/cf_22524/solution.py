"""
QUESTION:
Write a function called `split_and_reverse` that takes a sentence as input and returns a list of words. Each word in the resulting list should be reversed, and any punctuation marks should be removed from the words before they are reversed.
"""

import string

def split_and_reverse(sentence):
    """
    This function takes a sentence as input, splits it into words, removes punctuation, 
    and reverses each word.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: A list of reversed words with punctuation removed.
    """
    translator = str.maketrans('', '', string.punctuation)
    sentence_no_punct = sentence.translate(translator)
    words = sentence_no_punct.split()
    reversed_words = [word[::-1] for word in words]
    return reversed_words