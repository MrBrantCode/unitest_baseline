"""
QUESTION:
Create a function called `is_valid_sequence(sequence)` that checks whether the given string sequence is valid. A valid sequence starts and ends with a lowercase letter and consists of alternating lowercase letters and special characters, with no consecutive repeated characters. Special characters are defined as any character that is not a letter, digit, or whitespace.
"""

import re

def is_valid_sequence(sequence):
    pattern = re.compile(r'^[a-z]([a-z][^a-zA-Z0-9\s][a-z])*[^a-zA-Z0-9\s]?[a-z]$')
    
    if re.match(pattern, sequence):
        return True
    else:
        return False