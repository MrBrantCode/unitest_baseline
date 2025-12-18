"""
QUESTION:
Write a function `findSumPairs(v, sum)` that takes a list of integers `v` and an integer `sum` as input, and returns `True` if there exist any pairs of numbers in `v` that sum to `sum`, and `False` otherwise. The function should handle any list of integers and any possible sum value.
"""

def findSumPairs(nums, target_sum):  
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right: 
        if nums[left] + nums[right] == target_sum:
            return True
        elif nums[left] + nums[right] > target_sum:
            right -= 1
        else:
            left += 1
    return False