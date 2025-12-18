"""
QUESTION:
Write a function named `find_median` that takes an array of unique and positive integers as input, where the length of the array is an odd number, and returns the median of the array. The array is not guaranteed to be sorted.
"""

def find_median(arr):
    # Step 1: Sort the array in ascending order
    arr.sort()

    # Step 2: Find the middle index
    middle_index = (len(arr) - 1) // 2

    # Step 3: Return the value at the middle index
    return arr[middle_index]