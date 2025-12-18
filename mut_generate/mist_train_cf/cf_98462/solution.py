"""
QUESTION:
Write a function `extract_essential_words` that takes a sentence as input and returns a list of essential words "celebrate", "victory", "parade", and "tomorrow" in a case-insensitive manner. The function should account for possible variations in word order and punctuation, and exclude non-essential words.
"""

import re

def extract_essential_words(sentence):
    pattern = r"\b(celebrate|victory|parade|tomorrow)\b"
    return re.findall(pattern, sentence, flags=re.IGNORECASE)