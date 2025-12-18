"""
QUESTION:
Implement a function `binary_search` and a main function `find_value` that uses `binary_search` to retrieve the index of the first occurrence of a given item in a sorted array with unique non-negative values. The `binary_search` function must have a time complexity of O(log n) and implement the binary search algorithm recursively. The `find_value` function should handle cases where the item is not found and return an error message, and also handle cases where the item is present multiple times in the array by finding the first occurrence. The function should accept both integer and float values as input and be able to handle large arrays with up to 10^6 elements.
"""

def binary_search(arr, item, start, end):
    if start > end:
        return -1  # item not found
    mid = (start + end) // 2
    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return binary_search(arr, item, start, mid-1)
    else:
        return binary_search(arr, item, mid+1, end)

def find_value(arr, item):
    if len(arr) == 0:
        return "Array is empty"
    if item < 0:
        return "Item must be a non-negative value"
    index = binary_search(arr, item, 0, len(arr)-1)
    if index == -1:
        return "Item not found"
    while index > 0 and arr[index-1] == item:
        index -= 1
    return index