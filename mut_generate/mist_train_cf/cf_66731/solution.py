"""
QUESTION:
Develop a function named `detect_sequences` that takes three parameters: `text` (the input string), `sequences` (a list of sequences to search for), and `ignore_spaces` (a boolean flag indicating whether to ignore spaces in the text). The function should return a dictionary where each key is a sequence from the `sequences` list and its corresponding value is a list of positions where it's found in the `text`. The function should be case-insensitive, handle special characters and numbers, and return the correct positions even if `ignore_spaces` is True.
"""

import re

def detect_sequences(text, sequences, ignore_spaces=False):
    if ignore_spaces:
        text = text.replace(" ", "")
    text = text.lower() 
    sequences = [sequence.lower() for sequence in sequences] 

    result = {}
    for sequence in sequences:
        matches = [match.start() for match in re.finditer(re.escape(sequence), text)]
        result[sequence] = matches
    return result