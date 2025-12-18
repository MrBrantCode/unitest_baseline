"""
QUESTION:
Create a function called `remove_elements` that takes in a list of numbers and a value. The function should remove all elements of the list that are divisible by the given value in-place, without using built-in Python functions or methods that directly remove elements from a list, and return the modified list. If the given value is 0, the function should raise a ValueError. The function should handle cases where the given list is empty or does not contain any elements that are divisible by the given value by returning the original list unmodified.
"""

def remove_elements(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] % val == 0:
            nums.pop(i)
        else:
            i += 1
    
    return nums