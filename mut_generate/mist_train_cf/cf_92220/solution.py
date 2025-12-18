"""
QUESTION:
Write a function `count_occurrences` that takes a sorted array and a target element as input, and returns the number of times the target element appears in the array. The function should have a time complexity of O(log n), where n is the size of the array. The array can contain at most 10^6 elements and the target element will be a positive integer between 1 and 10^9 inclusive.
"""

def count_occurrences(arr, element):
    left = 0
    right = len(arr) - 1
    first_occurrence = -1
    last_occurrence = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            first_occurrence = mid
            right = mid - 1
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    if first_occurrence == -1:
        return 0

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            last_occurrence = mid
            left = mid + 1
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    return last_occurrence - first_occurrence + 1