"""
QUESTION:
Develop a function named `generate_permutations(N)` that produces a list of all permutations of the distinct numerical values from 1 to N.
"""

from itertools import permutations

def generate_permutations(N):
    values = list(range(1, N + 1))
    all_permutations = list(permutations(values))
    return all_permutations