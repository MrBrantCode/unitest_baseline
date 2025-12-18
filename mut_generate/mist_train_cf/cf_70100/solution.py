"""
QUESTION:
Implement a function `interpolation_search(list, y)` that performs an interpolative search for the target value `y` in a sorted list of integers, handling duplicates and missing numbers efficiently, and returns the index of `y` if found or -1 otherwise.
"""

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
        if arr[index] == target:
            return index

        if arr[index] < target:
            low = index + 1
        else:
            high = index - 1
    return -1