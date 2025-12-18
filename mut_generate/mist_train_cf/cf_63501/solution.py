"""
QUESTION:
Implement a function `ternary_search` that takes in a sorted array `arr`, left and right pointers `l` and `r`, and a target element `x`. Return the index of `x` in the array if found, and `-1` otherwise. The function should use ternary search algorithm and handle edge cases such as an empty array, single-element array, and `x` not present in the array.
"""

def ternary_search(arr, l, r, x):
    if r >= l: 
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        if arr[mid1] == x: 
            return mid1 
        if arr[mid2] == x: 
            return mid2 
        if x < arr[mid1]: 
            return ternary_search(arr, l, mid1-1, x) 
        elif x > arr[mid2]: 
            return ternary_search(arr, mid2+1, r, x) 
        else: 
            return ternary_search(arr, mid1+1, mid2-1, x)
    return -1