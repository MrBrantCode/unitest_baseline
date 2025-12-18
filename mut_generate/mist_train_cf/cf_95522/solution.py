"""
QUESTION:
Write a function named `binary_search_recursive` that implements a recursive binary search algorithm to find the index of the first occurrence of a given non-negative integer or float item in a sorted array containing unique elements. The function should have a time complexity of O(log n) and handle arrays with up to 10^6 elements. If the item is not found, the function should return an error message. The function should take four parameters: a sorted array `arr`, the target item, and the low and high indices of the current search range.
"""

def binary_search_recursive(arr, item, low, high):
    if low > high:
        return "Item not found"

    mid = (low + high) // 2

    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return binary_search_recursive(arr, item, low, mid - 1)
    else:
        return binary_search_recursive(arr, item, mid + 1, high)