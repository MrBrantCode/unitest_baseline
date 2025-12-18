"""
QUESTION:
Write a function `count_ones(ls)` that takes a list of integers as input where each integer is either 0 or 1 and returns the count of occurrences of the integer 1 in the list. The length of the input list does not exceed 10^5.
"""

from typing import List

def count_ones(ls: List[int]) -> int:
    count = 0
    for l in ls:
        if l == 1:
            count += 1
    return count