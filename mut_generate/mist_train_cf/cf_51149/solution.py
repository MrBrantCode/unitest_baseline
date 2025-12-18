"""
QUESTION:
Write a function `check_ascending(nums)` that takes a list of integers `nums` as input and returns `True` if the list contains unique elements in ascending order, and `False` otherwise.
"""

def check_ascending(nums):
    # Check for unique elements:
    if len(nums) != len(set(nums)):
        return False
    # Check for ascending order:
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True