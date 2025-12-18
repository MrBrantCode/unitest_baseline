"""
QUESTION:
Implement a function `count_integers(arr)` that takes a 2D array of integers as input and returns a tuple containing the total number of integers and the number of distinct integers in the array. The function should have a time complexity of at most O(n), where n is the total number of integers in the array. The array may contain lists of different lengths, negative integers, and duplicate integers.
"""

from typing import List, Tuple

def count_integers(arr: List[List[int]]) -> Tuple[int, int]:
    total = 0
    distinct = set()
    for sublist in arr:
        for num in sublist:
            total += 1
            distinct.add(num)
    return total, len(distinct)