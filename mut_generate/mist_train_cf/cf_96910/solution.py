"""
QUESTION:
Implement a function called `two_sum` that takes a list of integers `nums` and an integer `target` as input, and returns a list containing the indices of two numbers in the list that add up to the target. If no such pair is found, return "Target not found". The function should have a time complexity of O(n), where n is the length of the `nums` list.
"""

def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return "Target not found"