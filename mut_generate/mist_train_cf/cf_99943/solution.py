"""
QUESTION:
Write a Python function `extract_essential_words` that takes a sentence as input and returns a list of the essential words "celebrate", "victory", "parade", and "tomorrow" extracted from the sentence. The function should be case-insensitive and account for variations in word order and punctuation.
"""

import re

def extract_essential_words(sentence):
    """
    Extracts the essential words "celebrate", "victory", "parade", and "tomorrow" from a sentence.

    Args:
        sentence (str): The input sentence to extract words from.

    Returns:
        list: A list of the extracted essential words.
    """
    # Define the regular expression pattern
    pattern = r"\b(celebrate|victory|parade|tomorrow)\b"
    # Find all matches in the sentence
    matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
    # Return the matches
    return matches