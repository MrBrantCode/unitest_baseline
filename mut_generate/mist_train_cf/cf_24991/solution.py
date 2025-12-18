"""
QUESTION:
Write a function `generate_combinations` that takes a list of unique characters as input and returns all possible combinations of strings that can be formed using these characters. The function should return combinations of all lengths from 1 to the total number of characters.
"""

import itertools

def generate_combinations(chars):
    combinations = []
    for r in range(1, len(chars) + 1):
        combinations.extend([''.join(i) for i in itertools.permutations(chars, r)])
    return combinations