"""
QUESTION:
Create a function named `reverse_array` that takes an array of integers as input and returns a new array with the same elements in reverse order, without modifying the original array. The input array can be of any length and contain any integer values. The function should return a new array object, not modify the input array in-place.
"""

def reverse_array(nums):
    reversed_nums = []
    for i in range(len(nums)-1, -1, -1):
        reversed_nums.append(nums[i])
    return reversed_nums