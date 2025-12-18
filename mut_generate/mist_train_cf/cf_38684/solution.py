"""
QUESTION:
Create a function `max_difference` that takes a list of integers as input and returns the maximum difference between any two elements in the list. The difference is calculated by subtracting the smaller integer from the larger one. If the list contains fewer than two elements, the function should return 0.
"""

def max_difference(nums):
    if len(nums) < 2:
        return 0
    else:
        return max(nums) - min(nums)