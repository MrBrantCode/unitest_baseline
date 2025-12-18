"""
QUESTION:
Write a function called `remove_vowels_digits_punctuation_whitespace` that takes a string as input and returns a string containing only the consonants. The function should remove all vowels, digits, punctuation marks, and whitespace characters from the input string.
"""

import re

def remove_vowels_digits_punctuation_whitespace(text):
    # removing vowels
    text = re.sub(r'[aeiouAEIOU]', '', text)
    # removing digits
    text = re.sub(r'\d', '', text) 
    # removing punctuation
    text = re.sub(r'[^\w\s]', '', text) 
    # removing whitespace
    text = re.sub(r'\s', '', text)
    return text