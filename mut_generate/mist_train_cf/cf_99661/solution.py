"""
QUESTION:
Write a Python function `extract_essential_words` that takes a sentence as input and returns a list of the words "celebrate", "victory", "parade", and "tomorrow" if they appear in the sentence, regardless of order, punctuation, and capitalization, while excluding any non-essential words.
"""

import re

def extract_essential_words(sentence):
    """
    Extracts the words "celebrate", "victory", "parade", and "tomorrow" 
    from a sentence, regardless of order, punctuation, and capitalization.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: A list of extracted essential words.
    """
    pattern = r"\b(celebrate|victory|parade|tomorrow)\b"
    return re.findall(pattern, sentence, flags=re.IGNORECASE)