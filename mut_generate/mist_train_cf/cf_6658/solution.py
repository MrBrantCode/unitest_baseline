"""
QUESTION:
Implement a function named `binary_search_closest` that takes a sorted array `arr` and a target value `target` as input, and returns the number in the array closest to the target value. If the target value is present in the array, return it. If there are two numbers equally close to the target value, return the larger number. The array can be sorted in ascending or descending order and may contain duplicate values.
"""

def binary_search_closest(arr, target):
    low = 0
    high = len(arr) - 1
    closest = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]

        if closest is None or abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        elif abs(arr[mid] - target) == abs(closest - target) and arr[mid] > closest:
            closest = arr[mid]

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return closest