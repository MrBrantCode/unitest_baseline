"""
QUESTION:
Create a function named `find_combinations` that takes a string as input and returns a set of all unique combinations of letters from the string, where the order of the characters does not matter.
"""

from itertools import combinations

def find_combinations(input_string):
    unique_combinations = set()

    for r in range(1, len(input_string) + 1):
        combinations_object = combinations(input_string, r)
        for combination in combinations_object:
            unique_combinations.add(''.join(sorted(combination)))

    return unique_combinations