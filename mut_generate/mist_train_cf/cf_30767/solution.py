"""
QUESTION:
Write a function `find_max_number` that takes a list of integers as input and returns the maximum number in the list without using any built-in functions or methods that directly provide the maximum value.
"""

from typing import List

def find_max_number(arr: List[int]) -> int:
    max_num = arr[0]  # Initialize max_num with the first element of the list
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num