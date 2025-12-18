"""
QUESTION:
Develop a function `is_sorted(arr)` to determine if the given array is sorted in non-decreasing order. The array may contain duplicate elements. Implement this function using a single loop and with a space complexity of O(1).
"""

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True