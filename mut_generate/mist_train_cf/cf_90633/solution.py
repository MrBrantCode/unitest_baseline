"""
QUESTION:
Given an array of integers, write a function `find_duplicate(nums)` to find a duplicate element in the array without using any additional data structures. The function should return the duplicate element if found, and -1 if no duplicates are found.
"""

def find_duplicate(nums):
    # Sort the array to bring duplicate elements together
    nums.sort()

    # Iterate through the array to find duplicates
    for i in range(len(nums)-1):
        # If adjacent elements are equal, return the duplicate element
        if nums[i] == nums[i+1]:
            return nums[i]

    # If no duplicates found, return -1
    return -1