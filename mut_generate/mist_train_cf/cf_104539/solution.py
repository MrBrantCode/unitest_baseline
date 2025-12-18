"""
QUESTION:
Write a function `two_sum(nums, target)` that takes a list of integers `nums` and an integer `target` as input. The function should return the indices of the two numbers in the list that add up to the target sum. If no such pair is found, the function should return `None`.
"""

def two_sum(nums, target):
    num_dict = {}  # Hash table to store values and indices
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in num_dict:
            return [num_dict[complement], i]
        
        num_dict[nums[i]] = i
    
    return None