"""
QUESTION:
Create a function named `binary_search` that takes a sorted array and a number as input and returns the position of the number in the array using a recursive binary search algorithm with a time complexity of O(log n). If the number is not found in the array, return -1. The function should handle the case when the search range is specified by two indices, `low` and `high`, which define the search range within the array.
"""

def binary_search(arr, num, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == num:
        return mid
    elif arr[mid] < num:
        return binary_search(arr, num, mid+1, high)
    else:
        return binary_search(arr, num, low, mid-1)