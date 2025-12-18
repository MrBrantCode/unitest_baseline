"""
QUESTION:
Write a function named `find_oo_sequence` that takes a string sequence as input and returns `True` if the sequence consists only of letters and ends with "oo", and `False` otherwise. The function should be case-insensitive and consider only the alphanumeric characters and ignore special characters. The function should return `False` for sequences that contain numbers, special characters, or white spaces.
"""

import re

def find_oo_sequence(sequence):
    pattern = r'^[a-zA-Z]*oo$'
    return bool(re.search(pattern, sequence))