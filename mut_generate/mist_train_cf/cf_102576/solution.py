"""
QUESTION:
Write a function `find_duplicate` that takes a list of integers as input, finds the first duplicate element in the list, and returns it. If no duplicates are found, return -1. The function should handle duplicate elements and cannot use any additional data structures.
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