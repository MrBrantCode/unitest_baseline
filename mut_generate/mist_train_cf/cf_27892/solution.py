"""
QUESTION:
Write a function named `second_largest` that takes a list of integers `nums` as input and returns the second largest element in the list. The function should not use any built-in sorting functions or libraries.
"""

from typing import List

def second_largest(nums: List[int]) -> int:
    max_num = float('-inf')
    second_max_num = float('-inf')
    
    for num in nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    
    return second_max_num