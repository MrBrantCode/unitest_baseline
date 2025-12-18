"""
QUESTION:
Implement a function `ternary_search(arr, key, left, right)` that takes a sorted array `arr`, a target value `key`, and two indices `left` and `right` as input. The function should return the index of the `key` in the array if found, or -1 if not found. The function should use the ternary search algorithm, dividing the search space into thirds at each recursive step, until the `key` is found or the search space is exhausted.
"""

def ternary_search(arr, key, left, right):
    if right >= left:
        # Find the midpoints 
        mid1 = left + (right-left)//3
        mid2 = right - (right-left)//3

        # Check if key is present at any midpoints
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        # Since key is not present at midpoints, check in which region it may be present 
        if key < arr[mid1]:
            # The key lies between l and mid1 
            return ternary_search(arr, key, left, mid1-1)
        elif key > arr[mid2]:
            # The key lies between mid2 and r
            return ternary_search(arr, key, mid2+1, right)
        else:
            # The key lies between mid1 and mid2
            return ternary_search(arr, key, mid1+1, mid2-1)
    # Key is not present in array
    return -1