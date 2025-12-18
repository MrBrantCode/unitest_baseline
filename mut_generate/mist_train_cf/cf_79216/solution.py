"""
QUESTION:
Create a function `binary_search(arr, ele)` that checks if a certain element `ele` is present in a given array `arr` without using built-in array methods. The function should implement a binary search algorithm for better efficiency. Note that the array may not be initially sorted.
"""

def entance(arr, ele):
    arr.sort()   # required for binary search
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == ele:
            return True
        elif arr[mid] < ele:
            low = mid + 1
        else:
            high = mid - 1
    return False