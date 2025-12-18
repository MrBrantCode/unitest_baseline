"""
QUESTION:
Write a function `remove_vowels_digits_punctuation_whitespace(text)` that takes a string `text` and returns a string with all the vowels, digits, punctuation marks, and whitespace characters removed. The function should consider both lowercase and uppercase vowels ('a', 'e', 'i', 'o', 'u') and be case-sensitive.
"""

import re

def remove_vowels_digits_punctuation_whitespace(text):
    # Define the pattern for vowels, digits, punctuation marks, and whitespace characters.
    pattern = '[aeiouAEIOU0-9\s\W]'
    # Remove everything that matches the pattern.
    text = re.sub(pattern, '', text)
    return text