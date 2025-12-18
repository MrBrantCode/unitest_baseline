"""
QUESTION:
Write a function named `remove_element` that takes two parameters: an array of integers and an integer to remove from the array. The function should return the number of times the element was removed and modify the array in-place. The function should not use any built-in functions or methods that directly manipulate the array.
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
    
    nums[:] = nums[:next_position]
    
    return count