"""
QUESTION:
Create a function `detect_special_sequences` that takes a string as input and returns `True` if the string consists of only lowercase letters, digits, and exactly one '@' character, and `False` otherwise. The '@' character can appear at any position in the string.
"""

import re

def detect_special_sequences(input_string):
    pattern = r'^[a-z0-9]*@[a-z0-9]*$'
    match = re.fullmatch(pattern, input_string)
    return match is not None