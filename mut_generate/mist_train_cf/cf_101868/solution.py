"""
QUESTION:
Extract the essential words "celebrate", "victory", "parade", "tomorrow" from a given sentence using a regular expression in Python. The regular expression should take into account possible variations in word order, punctuation, and capitalization, and exclude any non-essential words. Write a function named `extract_essential_words` that accepts a string as input and returns a list of extracted essential words.
"""

import re

def extract_essential_words(sentence):
    """
    Extracts the essential words "celebrate", "victory", "parade", "tomorrow" from a given sentence.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        list: A list of extracted essential words.
    """
    # Define the regular expression pattern
    pattern = r"\b(celebrate|victory|parade|tomorrow)\b"
    # Find all matches in the sentence
    matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
    return matches