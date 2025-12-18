"""
QUESTION:
Implement a function `binary_search(arr, x)` that uses a binary search technique to find the lowest index of an element `x` in a sorted array `arr`. The function should be able to handle duplicate occurrences of integers in the array and return the index of the first occurrence of `x`. The array is chronologically ordered, meaning it is sorted in ascending order.
"""

def entrance(arr, x):
    left = 0
    right = len(arr) - 1
    result = -1
  
    while left <= right:
        mid = (left + right) // 2
  
        if arr[mid] == x:
            result = mid  
            right = mid - 1 
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
  
    return result