"""
QUESTION:
Write a function `find_missing_number(arr)` that finds the missing number in a sorted array of distinct integers. The function should have a time complexity of O(log n) and must not use any built-in functions, libraries, additional data structures, or arithmetic operations to find the missing number. The array will always contain at least three elements and the missing number will be between the minimum and maximum values of the array.
"""

def entance(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == mid + arr[0]:
            low = mid + 1
        else:
            high = mid - 1

    return arr[low] - 1