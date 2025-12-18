"""
QUESTION:
Design a function named `evaluate` that validates a given character sequence against a regex pattern. The sequence must be comprised of a non-whitespace minimum of 5 and a maximum of 20 characters. Additionally, the sequence must not hold more than 10 consecutive identical characters. The function should return a string indicating whether the sequence is valid or an error message describing the constraint that was not fulfilled.
"""

import re

def evaluate(seq):
    pattern = re.compile(r'\S{5,20}') 
    consecutive_pattern = re.compile(r'(.)\1{10,}')

    if not pattern.fullmatch(seq):
        return "Error: Character Sequence must be comprised of a non-whitespace minimum of 5 and a maximum of 20 characters."
    if consecutive_pattern.search(seq):
        return "Error: Character Sequence must not hold more than 10 consecutive identical characters."
    return "Character Sequence Valid."