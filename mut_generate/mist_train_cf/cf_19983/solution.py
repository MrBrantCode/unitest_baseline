"""
QUESTION:
Implement a function `search(arr, target, start, end)` that uses interpolation search to find the index of a given `target` element in a sorted `arr` array within the specified `start` and `end` indices. If the `target` element is not present in the array, return -1.
"""

def search(arr, target, start, end):
    if start > end or target < arr[start] or target > arr[end]:
        return -1

    position = start + ((end - start) // (arr[end] - arr[start])) * (target - arr[start])

    if arr[position] == target:
        return position

    if target < arr[position]:
        return search(arr, target, start, position - 1)

    return search(arr, target, position + 1, end)