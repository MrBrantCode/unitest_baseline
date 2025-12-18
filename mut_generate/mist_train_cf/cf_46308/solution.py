"""
QUESTION:
Write a function `compute_difference(set1, set2)` that takes two lists of integers as input, calculates the sum of each list, and returns the absolute difference between the two sums. The function should have a time complexity of O(n), where n is the total number of elements in both lists.
"""

from typing import List

def compute_difference(set1: List[int], set2: List[int]) -> int:
    return abs(sum(set1) - sum(set2))