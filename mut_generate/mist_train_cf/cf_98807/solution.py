"""
QUESTION:
Write a Python function named `find_frantic_sentences` that takes in a string `text` and returns a list of sentences containing the word 'frantic'. The function should use regular expressions to match sentences and handle edge cases such as abbreviations and acronyms.
"""

import re

def find_frantic_sentences(text):
    pattern = r'([A-Z][^\.!?]*frantic[^\.!?]*[\.!?])'
    matches = re.findall(pattern, text)
    return matches