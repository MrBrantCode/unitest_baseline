"""
QUESTION:
Write a Python function called "calculate_sum" that takes an array of integers as input and returns the sum of all its elements using a recursive approach. The function should have a base case that returns 0 for an empty array.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + calculate_sum(arr[1:])