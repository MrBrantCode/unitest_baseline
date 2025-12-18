"""
QUESTION:
Write a Python function named `multiply_and_sort` that takes a list of integers as input, multiplies each element by 3, and returns the resulting list in ascending order.
"""

def multiply_and_sort(nums):
    return sorted([num * 3 for num in nums])