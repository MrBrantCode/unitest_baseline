"""
QUESTION:
Write a function named `shortest_increasing_subarray` that takes a list of integers as input and returns the length of the shortest continuous increasing subarray. The subarray is considered increasing if each element is greater than the previous one. If there are no increasing subarrays, consider the single-element subarray as increasing.
"""

def shortest_increasing_subarray(nums):
    res, curr = float('inf'), 0
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]: 
            curr += 1
        else:
            res = min(res, curr + 1)
            curr = 0
    return min(res, curr + 1)