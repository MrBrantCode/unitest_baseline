"""
QUESTION:
Write a function `generate_combinations(string)` that generates all possible combinations of characters in a given string, considering both upper and lower case letters, and returns them as a list of strings.
"""

import itertools

def generate_combinations(string):
    # Create a list of characters from the given string
    chars = list(string)

    # Initialize an empty list to store the combinations
    combinations = []

    # Generate all possible combinations using itertools.product
    for r in range(1, len(chars) + 1):
        combinations.extend([''.join(comb) for comb in itertools.product(chars, repeat=r)])

    return combinations