"""
QUESTION:
Write a function named `modify_array` that takes an array of integers as input and returns a new array. In the new array, all elements greater than 5 should be incremented by 1, all elements equal to 0 should be removed, and any duplicate elements should be removed. The function must be implemented using a recursive approach. The input array can contain up to 1000 elements.
"""

def modify_array(arr):
    if len(arr) == 0:
        return []

    first = arr[0]
    if first == 0:
        return modify_array(arr[1:])

    if first > 5:
        first += 1

    modified_arr = modify_array(arr[1:])
    if first in modified_arr:
        return modified_arr

    return [first] + modified_arr