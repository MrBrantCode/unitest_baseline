"""
QUESTION:
Write a function named `reverse_text` that takes a string `input_text` as input, removes all punctuation, converts it to lowercase, and returns the string reversed character by character.
"""

import string

def reverse_text(input_text):
    # Remove punctuation
    s = input_text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    s = s.lower()
    # Reverse text
    s = s[::-1]
    return s