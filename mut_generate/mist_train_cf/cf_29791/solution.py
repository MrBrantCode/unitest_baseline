"""
QUESTION:
Write a function `count_unique_numbers` that takes a list of integers as input and returns the count of unique numbers in the list. A unique number is one that appears only once in the list. The input list will contain only integers and the function should return an integer.
"""

from typing import List

def count_unique_numbers(nums: List[int]) -> int:
    num_count = {}
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    return sum(1 for count in num_count.values() if count == 1)