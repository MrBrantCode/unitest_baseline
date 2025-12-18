"""
QUESTION:
Write a function named `remove_element` that takes an array of integers and an integer to be removed as input, removes all occurrences of the integer from the array in-place, and returns the number of times the integer was removed. The function should not use any built-in functions or methods that directly manipulate the array.
"""

def remove_element(nums, val):
    count = 0
    next_position = 0
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[next_position] = nums[i]
            next_position += 1
        else:
            count += 1
    
    nums[next_position:] = []  
    
    return next_position