"""
ORIGINAL QUESTION:
Implement a function `binary_search(lst, val)` that performs a binary search on a sorted list `lst` to find the index of the first occurrence of `val`. The function should work with lists sorted in either ascending or descending order and handle lists containing duplicate values by returning the index of the first occurrence.
"""

def binary_search(lst, val):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] < val:
            if lst[left] < lst[right]:  # Ascending order case
                left = mid + 1
            else:  # Descending order case
                right = mid - 1
        elif lst[mid] > val:
            if lst[left] < lst[right]:  # Ascending order case
                right = mid - 1
            else:  # Descending order case
                left = mid + 1
        else:
            # Check if the found index is the first occurrence
            if mid == 0 or lst[mid - 1] != val:
                return mid  # Return index of first occurrence
            else:
                right = mid - 1  # Continue searching on the left side
    return -1  # Value not found in list