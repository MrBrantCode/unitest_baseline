"""
QUESTION:
Implement a function named `process_array` that takes an array of integers as input and returns a modified array. If the input array is empty, return an empty array. For a non-empty array, modify each element as follows: if the number is even, square it; if the number is odd, cube it.
"""

from typing import List

def process_array(arr: List[int]) -> List[int]:
    return [num ** 2 if num % 2 == 0 else num ** 3 for num in arr]