"""
QUESTION:
Write a function `thirdMax(nums)` that takes an array of integers `nums` as input and returns the third highest unique number in the array. If the third highest unique number does not exist, return the highest number. Consider negative numbers as positive when determining the third highest number.

Restrictions:
- The length of `nums` is between 1 and 10^4 (inclusive).
- Each element in `nums` is a 32-bit signed integer.
- The function should have a time complexity of O(n).
"""

def thirdMax(nums):
    nums = list(set(nums))

    if len(nums) < 3:
        return max(nums)

    nums.remove(max(nums))
    nums.remove(max(nums))
    return max(nums)