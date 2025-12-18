"""
QUESTION:
Write a function `max_diff` that takes an array of integers as input and returns the maximum difference between two elements in the array where the larger element appears after the smaller element. The function should assume that the input array has at least one element.
"""

def max_diff(array):
    max_diff_val = 0
    min_val = array[0]

    for i in range(len(array)):
        if array[i] < min_val:
            min_val = array[i]
        else:
            max_diff_val = max(max_diff_val, array[i] - min_val)

    return max_diff_val