"""
QUESTION:
Implement a function named `reverse_list` that takes a list `arr`, a starting index `start`, and an ending index `end` as input. The function should reverse the elements of the list in-place using a recursive approach with O(1) space complexity. The input list may contain duplicate elements.
"""

def reverse_list(arr, start, end):
    if start >= end:
        return

    # Swap the first and last elements
    arr[start], arr[end] = arr[end], arr[start]

    # Reverse the remaining sublist
    reverse_list(arr, start+1, end-1)