"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list of numbers and a target number as input, and returns a list of indices where the target number appears in the list. If the target number is not found, return an empty list. The function should optimize for time complexity, and it should be able to handle duplicate elements in the list.
"""

def binary_search(arr, x):
    n = len(arr)
    mid = None

    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            break
    else:
        return []

    indices = [mid]
    i = mid - 1
    while i >= 0 and arr[i] == x:
        indices.append(i)
        i -= 1

    i = mid + 1
    while i < n and arr[i] == x:
        indices.append(i)
        i += 1

    return sorted(indices)