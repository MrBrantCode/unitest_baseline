"""
QUESTION:
Write a Python function `rec_sum` that recursively calculates the sum of all elements in a given array. The function should be able to handle arrays of any length, including empty arrays.
"""

def rec_sum(arr):
    # Base case: when array is empty
    if len(arr) == 0:
        return 0
    else:
        # Recursive case: first element + sum of the rest
        return arr[0] + rec_sum(arr[1:])