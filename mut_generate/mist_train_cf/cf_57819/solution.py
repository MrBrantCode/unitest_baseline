"""
QUESTION:
Implement the `trinarySearch` function that takes a sorted array `arr` and a target value `x` as inputs, and returns the index of `x` if it exists in `arr`, or -1 if it does not. The function should use a trinary search approach, dividing the array into three parts in each iteration.
"""

def trinarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid1 = low + (high-low)//3
        mid2 = high - (high-low)//3
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        if x < arr[mid1]:
            high = mid1 - 1
        elif x > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1