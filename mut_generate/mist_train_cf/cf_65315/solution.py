"""
QUESTION:
Create a function `remove_vowels_digits_punctuation_whitespace` that takes a string `text` as input. The function should return a string containing only the English consonant characters from the input string, excluding vowels, digits, punctuation marks, whitespace characters, and non-English alphabetical characters.
"""

import re
import string

def remove_vowels_digits_punctuation_whitespace(text):
    """
    Remove vowels, digits, punctuation marks, whitespace characters, and non-English alphabetical characters.
    Returns a string of only consonant non-punctuation non-whitespace English alphabet characters.
    """
    text = re.sub(r'[^A-Za-z\s]', '', text)                                      # Removing non-English alphabet characters and digits, but keeping whitespace characters for now.
    text = text.translate(str.maketrans('', '', string.punctuation))             # Removing punctuation.
    text = text.translate(str.maketrans('', '', string.whitespace))              # Removing whitespace characters.
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}                 # Set of English vowels.
    result = ''.join([char for char in text if char not in vowels])              # List comprehension to remove vowels.
    return result