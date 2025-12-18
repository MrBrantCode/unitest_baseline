"""
QUESTION:
Implement a function called `rotate` that takes two parameters: a list of elements and an integer `k`. Rotate the list to the right by `k` elements and return the resulting list. The function should handle cases where `k` is less than or equal to the length of the list.
"""

def rotate(nums, k): 
    k = k % len(nums)
    return nums[-k:] + nums[:-k]