"""
QUESTION:
Given an array of N integers, where N is up to 10^6 and integers range from -10^9 to 10^9, find the smallest missing positive number in the array. 

The function should handle duplicate numbers and return the smallest missing positive number. If no positive numbers are found, return N+1. The function must be implemented with O(N) time complexity and O(1) space complexity.

Implement the function find_smallest_missing_positive(arr), where arr is the input array of integers.
"""

def find_smallest_missing_positive(arr):
    n = len(arr)
    
    # Step 1: Mark presence of positive numbers
    for i in range(n):
        if arr[i] > 0 and arr[i] <= n:
            # Mark presence by modifying corresponding index
            arr[arr[i] - 1] = -abs(arr[arr[i] - 1])
    
    # Step 2: Find first index with a positive number
    for i in range(n):
        if arr[i] > 0:
            return i + 1
    
    # Step 3: No positive numbers found, return N+1
    return n + 1