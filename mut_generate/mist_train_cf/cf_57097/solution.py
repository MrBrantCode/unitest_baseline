"""
QUESTION:
Write a function `remove_vowels_digits_punctuation_whitespace_plus_count_consonants(text)` that takes a string `text` as input, removes all vowels, digits, punctuation marks, whitespace, and non-English letters from the string, and returns the count of consonants in the resulting string.
"""

import re

def remove_vowels_digits_punctuation_whitespace_plus_count_consonants(text):
    """
    remove_vowels_digits_punctuation_whitespace_plus_count_consonants is a function that intends to take in a string and produce an output string that ends up having no vowels, no digits, no punctuation marks, no whitespace, no non-English letters, and counts the number of consonants.
    """
    vowels="aeiouAEIOU"
    result=""
    for character in text:
        # Removing vowels, digits, punctuation, whitespace, and non-English letters
        if character not in vowels and character.isalpha():
            result += character
    # Removing any other non-letter characters
    result = re.sub(r'[^a-zA-Z]', '', result)
    # Counting the number of consonants
    consonants = len(result)
    return consonants