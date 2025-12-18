"""
QUESTION:
Write a function `find_missing_number(arr)` that finds the missing number in a sorted array of distinct integers with a time complexity of O(log n). The array will always contain at least three elements, and the missing number will be between the minimum and maximum values of the array. The function cannot use built-in functions, libraries, additional data structures, arithmetic operations, or mathematical formulas to find the missing number.
"""

def find_missing_number(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == mid + arr[0]:
            low = mid + 1
        else:
            high = mid - 1

    return arr[low] - 1