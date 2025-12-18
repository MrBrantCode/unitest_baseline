"""
QUESTION:
Implement a function `search(arr, target, start, end)` that uses interpolation search to find the index of a given element in a sorted array. The function should take a sorted array `arr`, the target element `target`, and the starting index `start` and ending index `end` as parameters. If the element is not present in the array, return -1. The array is 0-indexed and the function should use the interpolation search algorithm to find the index.
"""

def entrance(arr, target, start, end):
    if start > end or target < arr[start] or target > arr[end]:
        return -1

    position = start + ((end - start) // (arr[end] - arr[start])) * (target - arr[start])

    if arr[position] == target:
        return position

    if target < arr[position]:
        return entrance(arr, target, start, position - 1)

    return entrance(arr, target, position + 1, end)