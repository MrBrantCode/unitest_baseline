"""
QUESTION:
Write a function `next_greater_elements(nums: List[int]) -> List[int]` to return a list of integers representing the next greater element for each element in the input list `nums`, considering the circular nature of the list. If no greater element exists to the right, the output for that element should be -1.
"""

from typing import List

def next_greater_elements(nums: List[int]) -> List[int]:
    nums = nums + nums  # Duplicate the list to consider the circular nature
    stack = []  # Stack to store indices of elements
    out = [-1 for _ in nums]  # Initialize the output list with -1
    for index, num in enumerate(nums):
        while len(stack) and num > nums[stack[-1]]:
            out[stack.pop()] = num  # Update the output for elements with a next greater element
        stack.append(index)  # Push the current index onto the stack
    return out[:len(nums) // 2]  # Return the output for the original list length