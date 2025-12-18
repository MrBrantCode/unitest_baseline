"""
QUESTION:
Create a function named `reverse_array` that takes a list of integers as input and returns a new list with the same integers in reverse order without modifying the original list. The function should not use any built-in list reversal methods.
"""

def reverse_array(nums):
    reversed_nums = []
    for i in range(len(nums)-1, -1, -1):
        reversed_nums.append(nums[i])
    return reversed_nums