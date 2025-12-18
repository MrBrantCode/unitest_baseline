"""
QUESTION:
Given a list of integers `a`, write a function `sum_of_distinct_substrings` that calculates the sum of the lengths of all distinct substrings of `a`. The function should take a list of integers as input and return the sum of lengths as an integer. The list `a` will contain at least one element, and the function should be able to handle lists of varying lengths.
"""

from typing import List

def sum_of_distinct_substrings(a: List[int]) -> int:
    n = len(a)
    s = n * (n + 1) // 2  # Sum of all substrings
    return s