"""
QUESTION:
Write a function `calculate_sum(arr)` that takes an array of integers as an argument and returns the sum of its elements. The function should only use a single loop, modify the input array in-place to store the cumulative sum at each index, and not use any built-in functions or libraries for calculating the sum.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0

    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

    return arr[-1]