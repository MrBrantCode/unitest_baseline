"""
QUESTION:
Create a function `reverse_array` that takes a list of integers as input and returns a new list with the elements in reverse order. The function should not use any built-in functions for reversing or sorting. The input list can be of any length, but for the purpose of this problem, assume it will have at least one element.
"""

def reverse_array(nums):
    # Initialize an empty list
    reversed_nums = [0]*len(nums)
 
    # Iterate over the list in reverse order
    for i in range(len(nums)):
        # Assign each element to its new position
        reversed_nums[i] = nums[len(nums)-1-i]
 
    return reversed_nums