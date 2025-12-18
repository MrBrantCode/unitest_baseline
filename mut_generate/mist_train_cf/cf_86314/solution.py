"""
QUESTION:
Create a function named "sort_and_sum" that takes in a list of integers as a parameter, converts the list to a set of unique integers greater than 1, sorts the set in descending order, and returns the sum of the elements in the set.

The function should accept a list of up to 1000 integers, each ranging from -100 to 100, which may include duplicates, negative integers, and zero.
"""

from typing import List

def sort_and_sum(lst: List[int]) -> int:
    return sum(sorted({x for x in lst if x > 1}, reverse=True))