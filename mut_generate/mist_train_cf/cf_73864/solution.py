"""
QUESTION:
Write a function `remove_vowels_digits_punctuation_whitespace_plus` that accepts a string and returns a modified string devoid of vowels, digits, punctuation symbols, spaces, and non-English alphabets.
"""

import re

def remove_vowels_digits_punctuation_whitespace_plus(text):
    """
    remove_vowels_digits_punctuation_whitespace_plus is a function that accepts a string 
    and returns a modified string devoid of vowels, digits, punctuation symbols, spaces, 
    and non-English alphabets.
    """

    vowels = r'[aeiouAEIOU]'
    non_e_alphabets = r'[^a-zA-Z]'
    
    # Remove non English alphabets
    text = re.sub(non_e_alphabets, '', text)

    # Remove vowels
    text = re.sub(vowels, '', text)

    return text