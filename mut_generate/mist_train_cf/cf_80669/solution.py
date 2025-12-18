"""
QUESTION:
Generate all possible combinations of strings of length k that can be formed using the given list of unique characters, allowing for repetitions. 

Write a function named "string_combinations" that takes two parameters: a list of unique characters and an integer k, and returns a list of all possible string combinations. The function should be able to handle any length of the character list and any value of k.
"""

from itertools import product
from typing import List

def string_combinations(chars: List[str], k: int) -> List[str]:
    return [''.join(p) for p in product(chars, repeat=k)]