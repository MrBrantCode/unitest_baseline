"""
QUESTION:
Implement a function `recursive_sum(arr)` that calculates and prints the cumulative sum of all elements in a given 2-dimensional array `arr`. The function should be recursive and stop when the input array is empty. The array can have different number of elements in each subarray and the values will not be more than 1000.
"""

def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return sum(arr[0]) + recursive_sum(arr[1:])