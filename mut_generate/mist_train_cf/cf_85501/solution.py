"""
QUESTION:
Implement a recursive function named `three_way_search(arr, low, high, x)` that performs a three-way search on a sorted array `arr` to find the index of a given element `x`. The function should work for arrays of any type that can be sorted and compared, and it should return -1 if the element is not found.
"""

def three_way_search(arr, low, high, x):
    # Base case: if array is empty, return -1 (signifying the element is not found)
    if high < low:
        return -1

    # Divide the range [low, high] into three parts
    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    # Check if x is present at any mid
    if arr[mid1] == x:
        return mid1
    if arr[mid2] == x:
        return mid2
 
    # Since key is not present at mid,
    # check in which region it is present
    # then repeat the search in that region
    if x < arr[mid1]:
        return three_way_search(arr, low, mid1 - 1, x)
    elif x > arr[mid2]:
        return three_way_search(arr, mid2 + 1, high, x)
    else:
        return three_way_search(arr, mid1 + 1, mid2 - 1, x)