"""
QUESTION:
Write a Python function named `find_unique_digits` that takes two sequences (strings containing a mix of numerical and alphabetical characters) as input and returns a set of unique numerical elements found in both sequences.
"""

import re

def find_unique_digits(sequence1, sequence2):
    sequence1_digits = set(re.findall('\d', sequence1))
    sequence2_digits = set(re.findall('\d', sequence2))
    unique_digits = sequence1_digits.union(sequence2_digits)
    return unique_digits