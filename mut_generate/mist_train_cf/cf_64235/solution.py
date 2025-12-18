"""
QUESTION:
Implement a function `linear_search(arr, x)` that performs a linear search on a list of integers `arr` for a target integer `x`. The function should return the number of comparisons it took to find `x` if it exists in the list, and a message with the total number of comparisons if `x` is not found. The function should be optimized to stop searching as soon as `x` is found.
"""

def linear_search(arr, x):
    num_comp = 0
    for i in range(len(arr)):
        num_comp += 1
        if arr[i] == x:
            return num_comp
    return f'Number not found after {num_comp} comparisons'