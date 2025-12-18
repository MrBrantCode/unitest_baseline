"""
QUESTION:
Implement a recursive ternary search function in Python, named `ternary_search`, that takes a sorted one-dimensional array `arr`, a target element `x`, and two indices `left` and `right` as input. The function should return the index of the target element in the array if found, or -1 otherwise. Ensure that the function handles the case where the target element is not in the array.
"""

def ternary_search(arr, x, left, right):
    '''
    A recursive function to perform ternary search
    '''
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == x:  # First part has the target
            return mid1

        elif arr[mid2] == x:  # Second part has the target
            return mid2

        elif x < arr[mid1]:  # Target is in the first third.
            return ternary_search(arr, x, left, mid1 - 1)

        elif x > arr[mid2]:  # Target is in the third.
            return ternary_search(arr, x, mid2 + 1, right)

        else:  # Target is in the middle third.
            return ternary_search(arr, x, mid1 + 1, mid2 - 1)
    return -1