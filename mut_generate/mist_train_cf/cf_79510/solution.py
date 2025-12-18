"""
QUESTION:
Write a regular expression pattern in the `validate_sequence` function to match sequences that consist of alternating uppercase alphabets and numerical digits. The sequence must start with an uppercase letter, end with a digit, and contain at least one digit. The function should return `True` for valid sequences and `False` otherwise.
"""

import re

def validate_sequence(sequence):
    """
    Validate a sequence that consists of alternating uppercase alphabets and numerical digits.
    The sequence must start with an uppercase letter, end with a digit, and contain at least one digit.

    Args:
    sequence (str): The input sequence to be validated.

    Returns:
    bool: True if the sequence is valid, False otherwise.
    """
    pattern = r"^[A-Z]\d(?:[A-Z]\d)*$"
    return bool(re.match(pattern, sequence))