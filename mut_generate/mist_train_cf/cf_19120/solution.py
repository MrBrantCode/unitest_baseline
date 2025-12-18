"""
QUESTION:
Create a function `binary_search_recursive` that takes a sorted array `arr` and a target `item` as input, and returns the index of the first occurrence of `item` in `arr` using a recursive binary search algorithm. The array contains only unique non-negative integer and float values. The function should have a time complexity of O(log n) and be able to handle arrays with up to 10^6 elements. If the item is not found, the function should return an error message.
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