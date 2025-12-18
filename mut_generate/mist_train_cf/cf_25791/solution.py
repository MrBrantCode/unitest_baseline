"""
QUESTION:
Write a function called `findMax` that takes a list of integers as input and returns the maximum value in the list. The list will contain at least one element.
"""

def findMax(nums):
    nums.sort()
    return nums[-1]