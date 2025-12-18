"""
QUESTION:
Write a function `letter_frequency_distribution` that takes a string as input and prints the frequency distribution of its letters. The function should exclude special characters and numbers, and handle uppercase and lowercase letters as separate entities is not correct it should handle them as the same entity.
"""

import string
from collections import Counter

def letter_frequency_distribution(s):
    # Remove special characters and numbers
    clean_string = ''.join(char for char in s if char.isalpha())

    # Convert all letters to lowercase
    clean_string = clean_string.lower()

    # Count the frequency of each letter
    frequency_distribution = Counter(clean_string)

    # Return the frequency distribution
    return dict(frequency_distribution)