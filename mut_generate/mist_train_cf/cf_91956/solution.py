"""
QUESTION:
Write a function `get_words_without_vowels(sentence)` that takes a string sentence as input, uses regular expressions to parse and return a list of words from the sentence, and excludes any words that contain a vowel.
"""

import re

def get_words_without_vowels(sentence):
    # Define a regular expression pattern to match words
    pattern = r'\b[^\W\d_]+\b'
    
    # Find all words in the sentence that match the pattern
    words = re.findall(pattern, sentence)
    
    # Exclude words that contain a vowel
    words_without_vowels = [word for word in words if not re.search(r'[aeiou]', word, re.IGNORECASE)]
    
    return words_without_vowels