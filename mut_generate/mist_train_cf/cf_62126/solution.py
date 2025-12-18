"""
QUESTION:
Implement a function called `ternary_search` that takes an ordered list `arr` and a `key` to search for. The function should return the index of the key in the array if found, and -1 otherwise. The search should be performed using a ternary search technique, dividing the search space into three parts at each iterative step. The input array is guaranteed to be sorted.
"""

def ternary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while right >= left:
        mid1 = left + (right - left) // 3  
        mid2 = right - (right - left) // 3 
        if key == arr[mid1]:  
            return mid1
        if key == arr[mid2]:  
            return mid2
        if key < arr[mid1]:   
            right = mid1 - 1
        elif key > arr[mid2]:  
            left = mid2 + 1
        else:  
            left = mid1 + 1
            right = mid2 - 1
    return -1   # if key is not found in the array