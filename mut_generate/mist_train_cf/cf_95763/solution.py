"""
QUESTION:
Write a function `find_target(nums, target)` that takes an array of numbers `nums` and a target number `target` as input. The function should return a tuple containing a boolean value indicating whether the target number exists in the array and the index position of the first occurrence if it exists, or -1 if it does not.
"""

def find_target(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return True, i
    return False, -1