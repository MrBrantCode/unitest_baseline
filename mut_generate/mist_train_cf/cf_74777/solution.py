"""
QUESTION:
Implement a function `remove_vowels_digits_punctuation_whitespace(text)` that takes a string as input and returns a string with all vowels, digits, punctuation marks, and whitespace characters removed. The function should preserve the case of the original string and only retain the consonants.
"""

import string

def remove_vowels_digits_punctuation_whitespace(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    digits = string.digits
    punctuation = string.punctuation
    whitespace = string.whitespace

    new_text = ''.join([char for char in text if char not in vowels and char not in digits and char not in punctuation and char not in whitespace])
    
    return new_text