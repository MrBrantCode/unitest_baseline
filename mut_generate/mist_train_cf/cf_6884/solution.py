"""
QUESTION:
Write a recursive binary search function that finds the index of the first occurrence of a given target element in a sorted array of up to 10^9 elements. The function should have a time complexity of O(log n) and a space complexity of O(log n) in the worst case scenario, and return -1 if the target element is not present in the array.
"""

def entrance(arr, low, high, target):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        if mid == 0 or arr[mid - 1] < target:
            return mid
        else:
            return entrance(arr, low, mid - 1, target)

    elif arr[mid] < target:
        return entrance(arr, mid + 1, high, target)

    else:
        return entrance(arr, low, mid - 1, target)