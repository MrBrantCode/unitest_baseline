"""
QUESTION:
Write a function `count_and_indices(arr, target)` that returns a tuple containing the count and indices of all occurrences of `target` in a sorted array `arr`. The function should use a single loop and have a time complexity of O(log n), where n is the size of the array. The function should handle duplicate elements in the array efficiently and return the count and indices of the occurrences of the element. The array will contain at most 10^9 elements and the element to search for will be a positive integer between 1 and 10^9 inclusive.
"""

def count_and_indices(arr, target):
    left = binary_search(arr, target, True)
    if left == -1:
        return 0, []

    right = binary_search(arr, target, False)
    count = right - left + 1
    indices = [i for i in range(left, right + 1)]
    return count, indices

def binary_search(arr, target, find_leftmost):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            if find_leftmost:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result