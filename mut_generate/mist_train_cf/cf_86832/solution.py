"""
QUESTION:
Write a function `fetch_elements(arr, N)` that takes a list of integers `arr` and a positive integer `N` as input. The function should return the first `N` unique non-negative integers from `arr` in ascending order. If `arr` is empty, contains only negative numbers, or has less than `N` non-negative unique integers, the function should raise an exception. The function should have a time complexity of O(N log N).
"""

def fetch_elements(arr, N):
    if len(arr) == 0 or all(num < 0 for num in arr):
        raise Exception("Input array is empty or contains only negative numbers")
    
    # Remove negative elements and duplicates
    arr = list(set(filter(lambda x: x >= 0, arr)))
    
    if len(arr) < N:
        raise Exception("Input array does not have enough elements")
    
    # Sort the array in ascending order
    arr.sort()
    
    # Return the first N elements
    return arr[:N]