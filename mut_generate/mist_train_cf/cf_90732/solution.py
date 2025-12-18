"""
QUESTION:
Find the missing number in a sorted array of distinct integers with a single missing number between the minimum and maximum values. The function should have a time complexity of O(log n) and cannot use built-in functions, libraries, or additional data structures. The function name should be `find_missing_number` and it should take a sorted array `arr` as input.
"""

def find_missing_number(arr):
    difference = arr[0] - 0

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] - mid != difference:
            if arr[mid - 1] - (mid - 1) != difference:
                right = mid - 1
            else:
                return arr[mid] - 1
        else:
            if mid + 1 < len(arr) and arr[mid + 1] - (mid + 1) != difference:
                return arr[mid] + 1
            else:
                left = mid + 1

    return -1  # If no missing number is found