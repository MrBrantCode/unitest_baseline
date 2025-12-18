"""
QUESTION:
Write a function called `find_median` that takes an array of unique, positive integers as input, where the length of the array is an odd number. The function should return the median of the input array. The input array is not necessarily sorted.
"""

def find_median(arr):
    # Step 1: Sort the array in ascending order
    arr.sort()

    # Step 2: Find the middle index
    middle_index = (len(arr) - 1) // 2

    # Step 3: Return the value at the middle index
    return arr[middle_index]