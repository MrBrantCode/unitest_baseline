"""
QUESTION:
Implement a function `transform_list` that takes a list of integers as input and returns a new list where each element is transformed based on whether it is even or odd. If an integer is even, it should be divided by 2. If an integer is odd, it should be multiplied by 3 and then increased by 1. The function should return a new list with these transformations applied to each element.
"""

from typing import List

def transform_list(nums: List[int]) -> List[int]:
    transformed_nums = []
    for num in nums:
        if num % 2 == 0:  # If the integer is even
            transformed_nums.append(num // 2)
        else:  # If the integer is odd
            transformed_nums.append((num * 3) + 1)
    return transformed_nums