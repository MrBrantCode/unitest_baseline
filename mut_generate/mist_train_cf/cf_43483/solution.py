"""
QUESTION:
Write a function `min_difference(nums, target, i=0, memo=None)` that calculates the minimal difference possible from subtracting any combination of given numbers from a specified target. The function should be able to handle negative numbers and fractions. The numbers in the list can be used only once.
"""

def min_difference(nums, target, i=0, memo=None):
    if memo == None:
        memo = {}
    if target in memo:
        return memo[target]
    elif i == len(nums):
        memo[target] = abs(target)
    else:
        memo[target] = min(min_difference(nums, target - nums[i], i + 1, memo),
                            min_difference(nums, target, i + 1, memo))
    return memo[target]