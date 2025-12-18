"""
QUESTION:
Write a function `is_cyclic_symmetry(hex_seq)` that checks if a given sequence of hexadecimal characters is the same when reversed. The function should be case-insensitive and return a boolean value. The input sequence is assumed to be properly formed.
"""

def is_cyclic_symmetry(hex_seq):
    hex_seq = hex_seq.lower()  # Convert to lower case for consistency
    return hex_seq == hex_seq[::-1]