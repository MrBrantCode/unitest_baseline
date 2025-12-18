"""
QUESTION:
Write a function `smallest_disp` that takes a list of numbers as input and returns a tuple containing the smallest difference between any pair of elements in the list and the pair itself. The function should handle edge cases where the input list has less than two elements. The input list can contain duplicate values and is not guaranteed to be sorted.
"""

def smallest_disp(arr):
    if len(arr) < 2:
        return "The list should have at least two elements."
    arr.sort()  # this costs O(n log n) time
    min_diff = float('inf')
    res = (None, None)
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff
            res = (arr[i], arr[i+1])
    return min_diff, res