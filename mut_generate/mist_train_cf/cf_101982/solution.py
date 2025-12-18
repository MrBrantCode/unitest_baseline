"""
QUESTION:
Implement a function binary_search(arr, x) to find the index of an element x in a sorted array arr using binary search. The function should take two parameters: arr, a sorted list of integers, and x, the target integer. The function should return the index of x in arr if found, and -1 otherwise. The step size for updating the low and high indices should be 1.
"""

def entance(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1