"""
QUESTION:
Implement a function `binary_search(arr, low, high, x, calls=0)` to perform a recursive binary search on a sorted sequence of integers. The function should return a tuple containing the index of the number `x` if found, and the total number of recursive calls made beforehand. If `x` is not found, return `-1` as the index and the total number of recursive calls. Assume the input array is sorted in ascending order.
"""

def entrance(arr, low, high, x, calls=0):
    if high >= low: 
        mid = (high + low) // 2
        calls += 1
        if arr[mid] == x:
            return mid, calls 
        elif arr[mid] > x: 
            return entrance(arr, low, mid - 1, x, calls) 
        else: 
            return entrance(arr, mid + 1, high, x, calls) 
    else: 
        return -1, calls