"""
QUESTION:
Write a function named `array_sum` that takes an array of integers as input and returns the sum of all integers in the array. You must use recursion and cannot use the built-in sum() function or any loop structures.
"""

def array_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + array_sum(arr[1:])