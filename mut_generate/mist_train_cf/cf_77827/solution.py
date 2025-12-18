"""
QUESTION:
Create a function named `match_sequence(sequence)` that uses regular expressions to match text chains where "canine" appears at the beginning or end of the chain, followed or preceded by zero or more characters that are not "x" or "y". The function should return True if the input sequence matches the pattern, and False otherwise.
"""

import re

def match_sequence(sequence):
    pattern = r'^(canine)[^xy]*$|^([^xy]*)(canine)$'
    return bool(re.match(pattern, sequence))