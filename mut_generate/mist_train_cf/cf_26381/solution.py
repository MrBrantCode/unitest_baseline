"""
QUESTION:
Implement the `find_two_sum` function, which takes an array of integers `nums` and an integer `target` as input. The function should return an array of two distinct indices in `nums` that correspond to elements that sum up to `target`. If no such pair exists, return an empty array.
"""

def find_two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []