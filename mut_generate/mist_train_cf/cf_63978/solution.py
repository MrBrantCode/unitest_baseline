"""
QUESTION:
Implement a function `circularArraySearch(arr, x)` that takes a sorted array `arr` that has been circularly shifted and an element `x` as input, and returns the index of `x` in `arr` if it exists, or -1 if it does not. The function should have a time complexity of O(log n), where n is the length of the array.
"""

def circularArraySearch(arr, x):
    n = len(arr)
    
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] >= arr[low]:
            if x >= arr[low] and x < arr[mid]: 
                high = mid - 1
            else: 
                low = mid + 1

        elif arr[mid] <= arr[high]:
            if x > arr[mid] and x <= arr[high]: 
                low = mid + 1
            else: 
                high = mid - 1

    return -1