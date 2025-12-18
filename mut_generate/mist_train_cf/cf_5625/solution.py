"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array and an item as inputs and returns the index of the item in the array if it is found, or -1 if it is not found. The array is 0-indexed and the input array is already sorted in ascending order.
"""

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == item:
            return mid
        
        if item < arr[mid]:
            high = mid - 1
            if high < low:
                break
        else:
            low = mid + 1
            if low > high:
                break
    
    return -1