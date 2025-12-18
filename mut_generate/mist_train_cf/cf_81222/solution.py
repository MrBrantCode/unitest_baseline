"""
QUESTION:
Write a Python function `detect_sequence(input_string)` that takes a string `input_string` as input and returns a boolean indicating whether the string contains only uppercase letters and digits. The function should return `True` for strings like "AB12" and "45XY", and `False` for strings like "ab12", "45xy", and "@#$%". The function should also be extended to handle a list of input strings in a function `detect_sequences(input_list)`.
"""

import re

def detect_sequence(input_string):
    pattern = re.compile("^[A-Z0-9]+$")
    return bool(pattern.match(input_string))

def detect_sequences(input_list):
    results = []
    for input_string in input_list:
        results.append(detect_sequence(input_string))
    return results