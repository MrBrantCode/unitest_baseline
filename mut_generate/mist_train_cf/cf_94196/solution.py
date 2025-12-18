"""
QUESTION:
Create a function called `tokenize_sentence` that takes a string sentence as input. The function should remove any punctuation marks from the sentence, then tokenize the sentence into words that start with a capital letter. Return the list of tokenized words.
"""

import re

def tokenize_sentence(sentence):
    """
    Tokenize the given sentence into words starting with a capital letter.

    Args:
    sentence (str): The input sentence.

    Returns:
    list: A list of tokenized words.
    """
    # Remove punctuation marks
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Tokenize the sentence
    tokens = re.findall(r'\b[A-Z]\w+', sentence)

    return tokens