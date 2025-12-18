"""
QUESTION:
Implement a function `generate_combinations` that takes a list of integers as input and returns a list of lists, where each inner list represents a unique combination of the input items. The function should generate all possible combinations of the input list, including single elements and the full list itself. The input list will contain unique integers and may be empty. The function should be efficient in terms of time complexity.
"""

from typing import List

def generate_combinations(items: List[int]) -> List[List[int]]:
    result = []
    n = len(items)

    # Generate all possible combinations using bit manipulation
    for i in range(1 << n):
        combination = [items[j] for j in range(n) if (i & (1 << j))]
        result.append(combination)

    return result