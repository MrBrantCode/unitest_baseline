"""
QUESTION:
Write a function `count_occurrences` that takes a sorted array and a target element as input and returns the number of times the target element appears in the array. The function should have a time complexity of O(log n), where n is the size of the array, and should handle duplicate elements efficiently. The array can contain at most 10^9 elements and the target element is a positive integer between 1 and 10^9 inclusive.
"""

def count_occurrences(arr, target):
    def find_first_occurrence(low, high):
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def find_last_occurrence(low, high):
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    first = find_first_occurrence(0, len(arr) - 1)
    last = find_last_occurrence(0, len(arr) - 1)

    if first == -1 or last == -1:
        return 0
    return last - first + 1