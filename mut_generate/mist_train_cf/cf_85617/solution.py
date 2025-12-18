"""
QUESTION:
Write a function named `generate_permutations` that generates all possible arrangements of a given character sequence. The function should take a string `sequence` as input and return a list of all possible arrangements. The order of the arrangements does not matter. The function should handle sequences of any length, but be aware that the number of permutations grows factorially with the length of the sequence.
"""

import itertools

def generate_permutations(sequence):
    """
    Generate all possible arrangements of a given character sequence.

    Args:
        sequence (str): The input character sequence.

    Returns:
        list: A list of all possible arrangements of the input sequence.
    """
    return [''.join(p) for p in itertools.permutations(sequence)]