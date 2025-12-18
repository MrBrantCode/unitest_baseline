"""
QUESTION:
Write a function called `find_max_and_second_max` that finds the maximum and second maximum elements in a list of integers in a single iteration. The function should return `None` if the list has less than two elements. The function should not use any built-in functions or libraries for finding the maximum element. The list can contain both positive and negative integers and may have duplicate values.
"""

def entance(nums):
    if len(nums) < 2:
        return None

    max_val = nums[0]
    second_max_val = None

    for i in range(1, len(nums)):
        if nums[i] > max_val:
            second_max_val = max_val
            max_val = nums[i]
        elif second_max_val is None or nums[i] > second_max_val:
            second_max_val = nums[i]

    return max_val, second_max_val