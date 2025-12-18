"""
QUESTION:
Replace every element in the given array with the greatest element among the elements to its right, and replace the last element with -1. Return the array and the sum of the elements in the array.

The function name should be `replace_elements` and it takes one parameter, `arr`, which is a list of integers. The length of `arr` is between 1 and 10^4, and each element in `arr` is between 1 and 10^5.
"""

def replace_elements(arr):
    max_val = -1
    total = 0
    for i in range(len(arr) - 1, -1, -1):
        new_val = max(max_val, arr[i])
        arr[i] = max_val
        max_val = new_val
        total += arr[i]
    return arr, total