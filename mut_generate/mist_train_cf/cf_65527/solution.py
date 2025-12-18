"""
QUESTION:
Implement a function named `linear_search` that takes two parameters: a list of elements `arr` and a target element `x`. The function should return the index of `x` if it is found in `arr`, and -1 if `x` is not found in `arr`.
"""

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return index if element found
    return -1  # Return -1 if element not found in the list