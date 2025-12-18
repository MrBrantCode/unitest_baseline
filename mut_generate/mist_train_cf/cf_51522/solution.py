"""
QUESTION:
Implement a function named `binary_search` that uses a binary search algorithm to find a target integer within a sorted list of integers. The function should return the index of the target integer if it exists in the list; otherwise, it should return -1. The function must have a time complexity of O(log n) and should be implemented using recursive programming. The function should handle edge cases where the target integer is less than the smallest or greater than the largest integer in the list. The input parameters for the function are a sorted list of integers `arr`, the lowest index `low`, the highest index `high`, and the target integer `element`.
"""

def binary_search(arr, low, high, element):
    if high >= low: 
        mid = (high + low) // 2
  
        if arr[mid] == element: 
            return mid 
  
        elif arr[mid] > element: 
            return binary_search(arr, low, mid - 1, element) 
  
        else: 
            return binary_search(arr, mid + 1, high, element) 
  
    else: 
        return -1