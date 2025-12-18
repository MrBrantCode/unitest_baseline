"""
QUESTION:
Create a function `multiply_and_sort` that takes a list of integers as input, multiplies each element by its index, and returns the resulting list in descending order. The function should be implemented in Python.
"""

def multiply_and_sort(nums):
    return sorted([num * i for i, num in enumerate(nums)], reverse=True)