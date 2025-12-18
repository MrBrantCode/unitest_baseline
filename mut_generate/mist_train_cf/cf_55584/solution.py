"""
QUESTION:
Create a function `verify_sequence` that checks if a given string consists of interleaved uppercase letters and digits, starting with an uppercase letter and ending with a digit. The string must contain at least one digit.
"""

import re

def verify_sequence(sequence):
    pattern = re.compile(r'^[A-Z](?:[A-Z]*\d+[A-Z]*)*\d$')
    return bool(pattern.match(sequence))