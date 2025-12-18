"""
QUESTION:
Create a function called `detect_offensive_language` that takes two parameters: a sentence and a list of offensive words or phrases. The function should return `True` if the sentence contains any of the given offensive words or phrases and `False` otherwise. The function should handle variations in capitalization, punctuation, and special characters, as well as multi-word phrases that require specific word ordering. The list of offensive words or phrases can include words or phrases in multiple languages.
"""

import re

def detect_offensive_language(sentence, offensive_words):
    """
    Detects if a given sentence contains any of the provided offensive words or phrases.

    Parameters:
    sentence (str): The input sentence to check for offensive language.
    offensive_words (list): A list of offensive words or phrases.

    Returns:
    bool: True if the sentence contains any of the given offensive words or phrases, False otherwise.
    """
    # Convert the sentence to lowercase and remove punctuation marks
    sentence = re.sub(r'[^\w\s]', '', sentence).lower()

    # Iterate through each offensive word or phrase
    for word in offensive_words:
        # Remove special characters from the word and convert to lowercase
        word = re.sub(r'[^\w\s]', '', word).lower()
        
        # Check if the word is present in the sentence, accounting for multi-word phrases
        if word in sentence:
            return True

    # If no offensive words or phrases are found, return False
    return False