"""
QUESTION:
Write a Python function called `calculate_sum` that calculates the sum of all elements in a given array using a recursive approach. The function should take an array as input and return the sum of its elements. Assume the input array is a list of integers.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + calculate_sum(arr[1:])