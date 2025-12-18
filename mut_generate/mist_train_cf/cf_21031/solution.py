"""
QUESTION:
Implement a function named `calculate_sum` that takes an array of integers as input and returns the sum of all the numbers in the array. The array can contain both positive and negative integers. Do not use any built-in functions or methods that directly calculate the sum of an array, loops, or recursion.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + calculate_sum(arr[1:])