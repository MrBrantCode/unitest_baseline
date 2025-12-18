"""
QUESTION:
Implement a function `get_combinations_and_permutations` that takes a list of integers as input and returns all possible combinations and permutations of the integers, with each resulting subset comprising exactly three elements. The order of elements in combinations does not matter, while the order in permutations does. The function should use a subset size of three and assume that the input list contains at least three elements.
"""

import itertools

def get_combinations_and_permutations(numbers):
    combinations = list(itertools.combinations(numbers, 3))
    permutations = [list(itertools.permutations(comb)) for comb in combinations]
    return combinations, permutations