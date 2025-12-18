"""
QUESTION:
Write a function `array_sum` that takes an array of integers as input and returns their sum without using the built-in `sum()` function or any loop structures.
"""

def array_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + array_sum(arr[1:])