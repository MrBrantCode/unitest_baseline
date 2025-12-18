"""
QUESTION:
Create a function `get_words_without_vowels(sentence)` that takes a string sentence as input, uses regular expressions to parse the sentence into a list of words, and returns the list of words that do not contain any vowels. The function should treat uppercase and lowercase vowels the same.
"""

import re

def get_words_without_vowels(sentence):
    pattern = r'\b[^\W\d_]+\b'
    words = re.findall(pattern, sentence)
    words_without_vowels = [word for word in words if not re.search(r'[aeiou]', word, re.IGNORECASE)]
    return words_without_vowels