"""
QUESTION:
Create a function called `remove_vowels_digits_and_punctuation` that takes a string `text` as input and returns a string containing only the consonants from the input string. The function should remove all vowels, digits, and punctuation marks from the input string.
"""

import string

def remove_vowels_digits_and_punctuation(text):
    vowels = 'aeiouAEIOU'
    result = [char for char in text if char.isalpha() and char not in vowels]
    return ''.join(result)