"""
QUESTION:
Write a function `check_order(arr)` that determines whether the given array `arr` is in increasing order, decreasing order, or unordered. The function should return `1` if the array is in increasing order, `-1` if it's in decreasing order, and `0` if it's unordered. Assume that the array has at least two elements.
"""

def check_order(arr):
    order = 0
    if arr[0] < arr[1]:
        order = 1
    elif arr[0] > arr[1]:
        order = -1
    
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i+1] and order == 1:
            return 0
        elif arr[i] < arr[i+1] and order == -1:
            return 0
    return order