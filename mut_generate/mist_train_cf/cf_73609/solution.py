"""
QUESTION:
Generate all possible combinations of a given list of integers, including combinations of different integers across the list and combinations of successive integers. The function should be efficient enough to handle longer lists. The function name should be `generate_combinations`. The input is a list of integers and the output should include combinations of all lengths, including an empty combination.
"""

from itertools import combinations

def generate_combinations(numbers):
    result = []
    for i in range(len(numbers) + 1):
        result.extend(combinations(numbers, i))
    return [list(comb) for comb in result]