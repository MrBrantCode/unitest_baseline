"""
QUESTION:
Write a function `fetch_elements(arr, N)` that takes an array `arr` of integers and a positive integer `N` as input, and returns the first `N` non-negative unique elements from `arr` in ascending order. The function should raise an exception if `arr` is empty, contains only negative numbers, or does not have enough elements to fetch `N` non-negative unique elements. The function should have a time complexity of O(N log N), where N is the length of the input array `arr`.
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