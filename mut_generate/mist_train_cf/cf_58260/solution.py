"""
QUESTION:
Create a function named `check_sequence(sequence)` that takes a string of space-separated numerical sequences as input and returns a list of numerical sequences that fall within the range of 10 to 100, including single and double-digit integers. The function should use regular expressions to filter the numerical sequences and should not include any numbers outside the specified range or any partial matches within larger numbers.
"""

import re

def check_sequence(sequence):
    pattern = r'\b([1-9][0-9]?|100)\b'
    return [m.group(0) for m in re.finditer(pattern, sequence)]