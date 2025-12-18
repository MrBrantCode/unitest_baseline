"""
QUESTION:
Create a function named `match_character_sequence` that takes a string `sequence` as input and returns `True` if the string matches the character sequence 'abbccd' and `False` otherwise.
"""

import re

def match_character_sequence(sequence):
    pattern = re.compile('abbccd')
    match = pattern.match(sequence)
    
    if match:
        return True
    
    return False