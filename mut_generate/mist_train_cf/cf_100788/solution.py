"""
QUESTION:
Write a function named `extract_essential_words` that takes a string as input and returns a list of the essential words "celebrate", "victory", "parade", and "tomorrow" if they are present in the string. The function should be case-insensitive and ignore variations in word order and punctuation.
"""

import re

def extract_essential_words(sentence):
    """
    Extracts essential words "celebrate", "victory", "parade", and "tomorrow" from a given sentence.
    
    Args:
    sentence (str): The input sentence to extract essential words from.
    
    Returns:
    list: A list of essential words found in the sentence.
    """
    # Define the regular expression pattern
    pattern = r"\b(celebrate|victory|parade|tomorrow)\b"
    # Find all matches in the sentence
    matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
    # Return the matches
    return matches