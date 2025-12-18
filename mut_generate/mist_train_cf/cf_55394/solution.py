"""
QUESTION:
Create a function named `find_words_starting_with_ha` that takes a string `text` as input and returns a list of all words in the string that start with the characters "ha". The words should be matched as whole words only, not as parts of other words.
"""

import re

def find_words_starting_with_ha(text):
    pattern = r'\bha\w*\b'
    result = re.findall(pattern, text)
    return result