"""
QUESTION:
Write a function named `reverse_array` that takes a list of numbers as input and returns a new list with the elements in reverse order without using any built-in reverse or sorting functions.
"""

def reverse_array(nums):
    result = []
    for i in range(len(nums) -1, -1, -1):
        result.append(nums[i]) 
    return result