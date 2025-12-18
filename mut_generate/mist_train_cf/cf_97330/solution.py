"""
QUESTION:
Write a function called `calculate_sum` that takes an array as input and returns the sum of all elements using a recursive approach. The input array will contain a sequence of integers. The function should handle the base case where the input array is empty.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + calculate_sum(arr[1:])