"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array and an integer `x` as input, and returns the index of `x` in the array if found, or -1 if not found. The function should use the binary search algorithm to achieve this. The array is guaranteed to be sorted in ascending order.
"""

def binary_search(array, x):
    lower_bound = 0
    upper_bound = len(array) - 1
    index = -1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2

        if array[midpoint] < x:
            lower_bound = midpoint + 1
        elif array[midpoint] > x:
            upper_bound = midpoint - 1
        else:
            index = midpoint
            break

    return index