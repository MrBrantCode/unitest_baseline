"""
QUESTION:
Implement a recursive function named `binary_search` that takes in a sorted array `arr`, a target value `target`, and two indices `low` and `high`. The function should return the index of the target value in the array if it exists, or -1 if it doesn't. The time complexity of the function should be O(log n).
"""

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)