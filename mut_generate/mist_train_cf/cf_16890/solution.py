"""
QUESTION:
Given a list of unique numbers and a target number, create a function called `find_pairs` that takes the list and the target as input. The function should return the indices of the two elements in the list that sum to the target and have the smallest difference between them. If no such pair exists, the function should return an empty list. The time complexity of the solution should be O(n^2) and the space complexity should be O(1).
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