"""
QUESTION:
Create a function `are_permutations` that takes two character sequences as input and returns a boolean value indicating whether the sequences are permutations of each other. The function should handle case sensitivity and special characters.

Create another function `num_unique_permutations` that takes a single character sequence as input and returns the number of unique permutations that can be created from the sequence.

Implement these functions to efficiently calculate the permutations and account for repeated characters.
"""

from collections import Counter
from math import factorial

def are_permutations(str1, str2):
    """Checks if two character sequences are permutations of each other."""
    return Counter(str1) == Counter(str2)


def num_unique_permutations(seq):
    """Calculates the number of unique permutations that can be created from a sequence."""
    letter_counts = Counter(seq)
    result = factorial(len(seq))
    for count in letter_counts.values():
        result //= factorial(count)
    return result