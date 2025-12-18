"""
QUESTION:
Write a function `max_difference(nums)` that finds the maximum difference between any two elements in the given array of integers `nums`. The function should have a time complexity of O(n) and use only a constant amount of extra space. If the array has less than two elements, return 0.
"""

def max_difference(nums):
    if len(nums) < 2:
        return 0

    min_val = nums[0]
    max_diff = nums[1] - nums[0]

    for i in range(1, len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]
        elif nums[i] - min_val > max_diff:
            max_diff = nums[i] - min_val

    return max_diff