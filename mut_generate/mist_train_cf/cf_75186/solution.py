"""
QUESTION:
Write a function named `ternary_search` that takes a sorted array of integers `input_array` and a target integer `target` as input, and returns the index of `target` in `input_array` if it exists, or -1 otherwise. The function should divide the array into three equal parts and recursively search for the target in the appropriate section. The input array is assumed to be sorted in non-decreasing order.
"""

def ternary_search(input_array, left, right, target):
    if (right >= left):
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if input_array[mid1] == target:
            return mid1
        if input_array[mid2] == target:
            return mid2

        if target < input_array[mid1]:
            return ternary_search(input_array, left, mid1 - 1, target)
        elif target > input_array[mid2]:
            return ternary_search(input_array, mid2 + 1, right, target)
        else:
            return ternary_search(input_array, mid1 + 1, mid2 - 1, target)
    return -1