"""
QUESTION:
Create a function named `extract_long_words` that uses regular expressions to extract all words with a minimum of 7 characters from a given sentence.
"""

import re

def extract_long_words(sentence):
    pattern = r'\b\w{7,}\b'
    matches = re.findall(pattern, sentence)
    return matches