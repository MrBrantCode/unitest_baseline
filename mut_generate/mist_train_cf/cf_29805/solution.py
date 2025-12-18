"""
QUESTION:
Implement a function `generate_combinations(elements)` that takes a list of unique elements as input and returns a list of lists, where each inner list represents a unique combination of elements. The function should generate all possible combinations of the input elements, where the order of selection does not matter and the input list does not contain duplicate elements. The output list can be in any order.
"""

from itertools import combinations

def generate_combinations(elements):
    all_combinations = []
    for r in range(1, len(elements) + 1):
        all_combinations.extend(list(combinations(elements, r)))
    return [list(comb) for comb in all_combinations]