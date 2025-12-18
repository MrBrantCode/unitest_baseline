"""
QUESTION:
Implement the `remove_pool` function, which takes two parameters: `pool` (a list of integers) and `criteria` (a list of integers). The function should remove all elements from the `pool` that are divisible by any of the numbers in the `criteria` list and return the modified pool.
"""

from typing import List

def remove_pool(pool: List[int], criteria: List[int]) -> List[int]:
    return [x for x in pool if all(x % c != 0 for c in criteria)]