"""
QUESTION:
Implement the `generate_unique_combinations(chars)` function, where `chars` is a set of characters. The function should return a list of all unique combinations of these characters, with no repetition of characters within each combination.
"""

from itertools import permutations

def generate_unique_combinations(chars):
    # Generate all permutations of the characters
    all_permutations = permutations(chars)

    # Convert each permutation to a string and store unique combinations
    unique_combinations = [''.join(perm) for perm in set(all_permutations)]

    return unique_combinations