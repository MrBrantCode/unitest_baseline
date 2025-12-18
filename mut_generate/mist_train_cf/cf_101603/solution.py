"""
QUESTION:
Write a function `extract_essential_words` that takes a string `sentence` as input and extracts the words "celebrate", "victory", "parade", and "tomorrow" from it, considering possible variations in word order, punctuation, and capitalization. The function should return a list of the extracted words.
"""

import re

def extract_essential_words(sentence):
    """
    Extracts the words "celebrate", "victory", "parade", and "tomorrow" from a given sentence,
    considering possible variations in word order, punctuation, and capitalization.

    Args:
        sentence (str): The input sentence to extract words from.

    Returns:
        list: A list of the extracted words.
    """
    pattern = r"\b(celebrate|victory|parade|tomorrow)\b"
    matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
    return matches