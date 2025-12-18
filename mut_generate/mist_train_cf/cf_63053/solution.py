"""
QUESTION:
Implement a function named `interpolation_search` that performs the Interpolation Search algorithm on a sorted list of numbers to find a given target value. The function should take two parameters: a sorted list `arr` and a target value `x`. It should return the index of the target value if found, and -1 otherwise. The function should handle edge cases and potential errors.
"""

def interpolation_search(arr, x):
    low = 0
    high = (len(arr) - 1)

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + ((high - low) // (arr[high] - arr[low]) *
                     (x - arr[low]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1