"""
QUESTION:
Implement a function `twoSum` that takes an array of integers `nums` and a target value `target`, and returns a list of two indices that add up to the target. You can assume that the input array will always have at least two elements, and the target value will always have a valid pair of indices. The indices are 0-based, and the array may contain duplicate values, but the target value will always have a unique pair of indices.
"""

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]