"""
QUESTION:
Write a function named `find_max_index` that takes an array of integers as input and returns the maximum value and its index in the array without using any built-in or imported functions. The function should assume the input array is non-empty and contain at least one element.
"""

def find_max_index(arr):
    # Initialize the max_val to the first element in arr,
    # and assign 0 as the initial index
    max_val = arr[0]
    max_index = 0

    for i in range(1, len(arr)):
        # If arr[i] is bigger than max_val, set max_val to arr[i],
        # and assign i as the new index
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    return max_val, max_index