"""
QUESTION:
Given a list of unique numbers and a target number, create a function named `find_pairs(nums, target)` that finds the indices of the two elements with the smallest difference that sum up to the target number. If no such pair exists, return an empty list. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def find_pairs(nums, target):
    n = len(nums)
    min_diff = float('inf')
    indices = []

    for i in range(n):
        for j in range(i+1, n):
            diff = abs(nums[i] - nums[j])
            if nums[i] + nums[j] == target and diff < min_diff:
                min_diff = diff
                indices = [i, j]

    return indices