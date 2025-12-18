"""
QUESTION:
Implement a function `binary_search(arr, x)` that takes a sorted list `arr` and an element `x` as input, and returns the number of occurrences of `x` in `arr`. The function should be efficient in terms of time and space complexity.
"""

def binary_search(arr, x):
    n = len(arr)
    first_occurrence = find_occurrence(arr, n, x, True)
    last_occurrence = find_occurrence(arr, n, x, False)
    
    # If element is not present in the list
    if first_occurrence != -1:
        return last_occurrence - first_occurrence + 1
    else:
        return "Element not found in array"

def find_occurrence(arr, n, x, findFirst):
    start = 0; end = n - 1
    result = -1
    while (start <= end):
        mid = int((start + end) / 2)
        if arr[mid] == x:
            result = mid
            if findFirst:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return result