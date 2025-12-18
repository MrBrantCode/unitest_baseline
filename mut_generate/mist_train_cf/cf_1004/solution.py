"""
QUESTION:
Implement a function `find_max` that uses the divide and conquer approach to find the maximum element in an array of integers. The function should divide the array into two halves, find the maximum element in each half recursively, and return the maximum element of the entire array. The function should handle the base case where the array has only one element. The array can contain duplicate elements, and the maximum element can appear at any position in the array.
"""

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    
    return max(left_max, right_max)