"""
QUESTION:
Write a function named `second_smallest` that takes a list of integers as input and returns the second smallest unique number. If the list has less than two unique numbers, return "Invalid list: list must contain at least two unique numbers." The function should handle lists with duplicate numbers, negative numbers, and be efficient for large lists.
"""

def entrance(nums):
    if len(nums) < 2: 
        return "Invalid list: list must contain at least two unique numbers."
   
    nums_set = set(nums)
    if len(nums_set) < 2: 
        return "Invalid list: list must contain at least two unique numbers."
      
    return sorted(nums_set)[1]