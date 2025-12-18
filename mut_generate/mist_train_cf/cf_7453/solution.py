"""
QUESTION:
Write a function `is_order(arr)` that determines whether the given array is strictly increasing, strictly decreasing, non-decreasing, non-increasing, or unordered without using comparison operators, sorting algorithms, or additional data structures. The array is 1D and contains integers. The function should return a string describing the order of the array.
"""

def is_order(arr):
    # Helper function to check if all elements in the array are equal
    def all_equal(start, end):
        if start == end:
            return True
        return arr[start] == arr[start + 1] and all_equal(start + 1, end)

    # Helper function to check if all elements in the array are in a certain order
    def is_in_order(start, end, increasing=True):
        if start == end:
            return True
        if increasing:
            return arr[start] <= arr[start + 1] and is_in_order(start + 1, end, increasing)
        else:
            return arr[start] >= arr[start + 1] and is_in_order(start + 1, end, increasing)

    length = len(arr)

    # Base cases
    if length <= 1:
        return "Unordered"
    elif all_equal(0, length - 1):
        return "Unordered"
    elif is_in_order(0, length - 1, True):
        if is_in_order(0, length - 1):
            return "Strictly Increasing"
        else:
            return "Non-decreasing"
    elif is_in_order(0, length - 1, False):
        if is_in_order(0, length - 1, False):
            return "Strictly Decreasing"
        else:
            return "Non-increasing"
    else:
        return "Unordered"