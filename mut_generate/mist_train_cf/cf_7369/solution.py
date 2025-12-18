"""
QUESTION:
Write a function named `find_max_min` that takes an array of integers as input and returns a tuple containing the maximum and minimum values in the array. The array can have duplicate values and can be of any length between 1 and 10^6. The function should not use any built-in sorting functions or data structures and should run in linear time, i.e., O(n), where n is the length of the array.
"""

def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    return max_val, min_val