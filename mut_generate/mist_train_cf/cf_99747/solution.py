"""
QUESTION:
Write a function named `find_frantic_sentences` that takes a string `text` as input and returns a list of sentences containing the word 'frantic'. The function should use regular expressions to match sentences and handle edge cases such as abbreviations and acronyms. The function should not require any additional input parameters and should only rely on the provided text.
"""

import re
def find_frantic_sentences(text):
    pattern = r'([A-Z][^\.!?]*frantic[^\.!?]*[\.!?])'
    matches = re.findall(pattern, text)
    return matches