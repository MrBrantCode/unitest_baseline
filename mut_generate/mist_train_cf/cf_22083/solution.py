"""
QUESTION:
Implement a function named `two_sum` that takes a list of integers `nums` and a target integer `target` as input. The function should return the indices of the two numbers in the `nums` list that add up to the `target`. If no such pair is found, the function should return "Target not found". The function should have a time complexity of O(n), where n is the length of the `nums` list.
"""

def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return "Target not found"