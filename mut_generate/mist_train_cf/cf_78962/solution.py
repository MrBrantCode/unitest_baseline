"""
QUESTION:
Implement a function binary_search that performs a recursive binary search on a sorted array. The function should take four parameters: a sorted array, a lower bound index, an upper bound index, and a target key. It should return the index of the target key if found, otherwise -1. The function should not include the lower bound index in the next recursive call if the target key is less than the middle element. The function should not include the middle element in the next recursive call if the target key is greater than the middle element.
"""

def binary_search(arr, low, high, key):
    if high < low:
        return -1
    
    mid = low + (high - low) // 2
    
    if key < arr[mid]:
        return binary_search(arr, low, mid-1, key)
    elif key > arr[mid]:
        return binary_search(arr, mid+1, high, key)
    else:
        return mid