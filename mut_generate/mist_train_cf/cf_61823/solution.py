"""
QUESTION:
Given an array `nums` of `n` integers, determine the least number of steps needed to make all elements in the array identical. In each step, you are allowed to either increment `n - 1` elements of the array by `1` or decrement `1` element of the array by `1`. The length of `nums` is between 1 and 10^4, inclusive, and the elements in `nums` range from -10^9 to 10^9, inclusive. Define a function `min_steps(nums)` that returns the minimum number of steps required to equalize the elements in the array.
"""

def min_steps(nums):
    nums.sort()
    steps = 0
    for num in nums:
        steps += abs(num - nums[0])
    return steps