"""
QUESTION:
Write a function `find_pairs(array, target)` that finds all pairs of elements in the given array whose sum is equal to the target value. The function should return a list of all such pairs and have a time complexity of O(n^2), without using any built-in sorting functions.
"""

def entance(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append((nums[i], nums[j]))
    return res