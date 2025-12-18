"""
QUESTION:
Given an array `arr` of integers and an integer `limit`, find the minimum number of elements that need to be changed to make the array palindromic, with a constraint that the limit of distinct element changes cannot exceed 50% of the array length. The function `smallest_change(arr, limit)` should return the minimum number of changes required.
"""

def smallest_change(arr, limit):
    n = len(arr)
    limit = min(limit, n // 2)  # Ensure limit does not exceed 50% of array length
    
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            changes += 1
        if changes > limit:
            break
    return min(changes, limit)