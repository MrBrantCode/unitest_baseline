"""
QUESTION:
Create a function `is_sorted(arr)` that checks if a given array `arr` is sorted in non-decreasing order. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def is_sorted(arr):
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    
    return True