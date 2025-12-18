"""
QUESTION:
Create a function named `compare_word_sequence` that takes two string parameters `phrase1` and `phrase2`. The function should compare the word sequences in the two input phrases, considering the multiplicity of words, character casing, punctuation, and the order of the words. It should return a boolean value indicating whether the word sequences are identical.
"""

import string

def compare_word_sequence(phrase1: str, phrase2: str) -> bool:
    # Remove punctuation and convert to lower case
    phrase1 = phrase1.translate(str.maketrans('', '', string.punctuation)).lower().split()
    phrase2 = phrase2.translate(str.maketrans('', '', string.punctuation)).lower().split()

    # Compare the two phrases
    return phrase1 == phrase2