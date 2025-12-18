"""
QUESTION:
Create a function that takes a list of integers as input and returns the maximum and minimum values in the list. The function should be able to handle an empty list, in which case it should return a tuple with two None values. The function should also handle a list with a single element, in which case it should return a tuple with the same value twice. The function should not use the built-in max and min functions in Python.

Restrictions: 
- Do not use the built-in max and min functions in Python.
"""

def entrance(nums):
    if not nums:
        return None, None
    min_val = max_val = nums[0]
    for num in nums[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val