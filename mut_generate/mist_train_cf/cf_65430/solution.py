"""
QUESTION:
Generate all possible sequences of length k using characters from a given set of lowercase alphabets.

Function name: generate_sequences
Input parameters: set_val (a set of lowercase alphabets), k (length of each sequence)
Restriction: The sequences should only contain characters from the given set and their length should be equivalent to k.

Example: If set_val = {'a', 'b', 'c'} and k = 3, the function should return all possible sequences of length 3 using characters 'a', 'b', and 'c'.
"""

from itertools import product

def generate_sequences(set_val, k):
    return [''.join(p) for p in product(set_val, repeat=k)]