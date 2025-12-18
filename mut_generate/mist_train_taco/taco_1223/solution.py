"""
QUESTION:
An array is said to be `hollow` if it contains `3` or more `0`s in the middle that are preceded and followed by the same number of non-zero elements. Furthermore, all the zeroes in the array must be in the middle of the array. 

Write a function named `isHollow`/`is_hollow`/`IsHollow` that accepts an integer array and returns `true` if it is a hollow array,else `false`.
"""

def is_hollow(arr):
    # Remove all leading and trailing non-zero elements
    while arr and arr[0] != 0 and arr[-1] != 0:
        arr = arr[1:-1]
    
    # Check if the remaining array has 3 or more zeros and all elements are zeros
    return len(arr) >= 3 and set(arr) == {0}