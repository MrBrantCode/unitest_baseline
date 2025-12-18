"""
QUESTION:
Implement a function `sort_array(arr)` that sorts the input array `arr` in descending order using only a single loop.
"""

def sort_array(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr