"""
QUESTION:
Create a function `rearrange_two_elements(arr)` that takes an array of integers as input and returns `True` if it is possible to rearrange the array into non-decreasing order by swapping exactly two pairs of elements, and `False` otherwise. The function should also return `True` for an empty array.
"""

def rearrange_two_elements(arr):
    n = len(arr)
    if n == 0: # check if list is empty
        return True
    # create a sorted copy of list
    sorted_arr = sorted(arr)

    mismatched = [] # initialize a list to capture mismatched elements
    for i in range(n):
        # check mismatch between original list and sorted list
        if arr[i] != sorted_arr[i]:
            mismatched.append((arr[i], sorted_arr[i]))

    mismatch_count = len(mismatched)

    if mismatch_count == 0 or mismatch_count == 2:
        return True
    else:
        return False