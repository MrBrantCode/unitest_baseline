"""
QUESTION:
Extract the words "celebrate", "victory", "parade", and "tomorrow" from a sentence while ignoring word order, punctuation, and capitalization using a regular expression. Write a function named `extract_essential_words` that takes a sentence as input and returns a list of the extracted words.
"""

import re

def extract_essential_words(sentence):
    """
    Extracts the essential words 'celebrate', 'victory', 'parade', 'tomorrow' from a sentence.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        list: A list of the extracted essential words.
    """
    # Define the regular expression pattern
    pattern = r"\b(celebrate|victory|parade|tomorrow)\b"
    # Find all matches in the sentence
    matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
    return matches