"""
QUESTION:
Create a function `is_offensive` that takes two parameters: a sentence and a list of offensive words or phrases. The function should return `True` if the sentence contains any of the offensive words or phrases (ignoring variations in capitalization and punctuation) and `False` otherwise. The function should be case-insensitive and able to handle phrases.
"""

import string

def is_offensive(sentence, offensive_words):
    """
    Checks if a sentence contains any of the given offensive words or phrases.

    Args:
    sentence (str): The input sentence to check.
    offensive_words (list): A list of words or phrases to consider as offensive.

    Returns:
    bool: True if the sentence contains any offensive words, False otherwise.
    """
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    
    for word in words:
        if word in [x.lower() for x in offensive_words]:
            return True
    
    for phrase in offensive_words:
        if phrase.lower() in sentence:
            return True

    return False