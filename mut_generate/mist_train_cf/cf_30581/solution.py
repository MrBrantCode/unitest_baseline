"""
QUESTION:
Implement a function named `manipulate_list` that takes a list of integers as input, removes all even numbers, doubles the value of each remaining number, and sorts the list in ascending order. The function should return the modified list. The input list will only contain integers, and the function must not modify the original list.
"""

from typing import List

def manipulate_list(nums: List[int]) -> List[int]:
    # Remove all even numbers from the list
    nums = [x for x in nums if x % 2 != 0]
    
    # Double the value of each remaining number
    nums = [x * 2 for x in nums]
    
    # Sort the list in ascending order
    nums.sort()
    
    return nums