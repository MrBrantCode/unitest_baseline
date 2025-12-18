"""
QUESTION:
Write a function `calculate_sum` that takes an array of integers as input and returns the sum of its elements. The function should work with arrays of any size, handle empty arrays, use only a single loop to iterate through the array, and not use any built-in sum functions or libraries. The function should modify the input array in-place to store the cumulative sum at each index and return the sum without using any temporary variables.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0

    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

    return arr[-1]