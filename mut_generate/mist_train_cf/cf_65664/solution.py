"""
QUESTION:
Write a function named `second_smallest` that takes a list of numbers as input. The function should return the second smallest unique number in the list. If the list is empty, contains only one element, or has less than two unique elements, return an error message.
"""

def second_smallest(nums):
    if len(nums) == 0:
        return "List is empty"
    if len(nums) == 1:
        return "List contains only one element"
    
    # using set to remove duplicate then convert back to list
    nums = list(set(nums))

    nums.sort()
    if len(nums) < 2:
        return "No second unique number available in the list"
    
    return nums[1]  # Return the second smallest number