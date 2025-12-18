"""
QUESTION:
Create a function `check_sequence(seq)` that takes a string `seq` as input and returns a boolean value. The function should return `True` if the input string consists of a sequence of alternating lowercase letters and special characters (non-alphanumeric characters), and ends with a lowercase letter. The function should return `False` otherwise.
"""

import re

def check_sequence(seq):
    pattern = '^([a-z][^a-zA-Z0-9])*[a-z]$'
    return bool(re.search(pattern, seq))