"""
QUESTION:
Implement a function called `binary_search` that takes in four parameters: `arr`, `low`, `high`, and `x`, where `arr` is a sorted list, `low` and `high` represent the search interval, and `x` is the target value to be found in the list. The function should return the index of `x` if found, and -1 otherwise. Assume that the input list `arr` is sorted in ascending order.
"""

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
  
        if arr[mid] == x:
            return mid
  
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
  
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1