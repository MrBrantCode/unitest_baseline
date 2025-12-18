"""
QUESTION:
Write a function `count_monosyllabic_words` that takes a sentence as input and returns the number of monosyllabic words. A word is considered monosyllabic if it has a single vowel sequence or a single semivowel ('y', 'w') followed by any number of consonants. The function should have a time complexity of O(n), where n is the length of the input sentence.
"""

import re

def count_monosyllabic_words(sentence):
    # Regex pattern to match words with a single vowel sequence or 
    # a single semivowel followed by any number of consonants
    pattern = r'\b[^aeiouyw]*([aeiouyw])[^\s]*\b'
    
    words = re.findall(pattern, sentence, re.IGNORECASE)
    
    return len(words)