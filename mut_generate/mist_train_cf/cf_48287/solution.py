"""
QUESTION:
Create a function named `binary_search` that takes two parameters: `arr` (a sorted list of integers) and `x` (an integer to be searched). Implement an iterative binary search technique to find the range of indices where `x` appears in `arr`, considering cases where `x` may appear multiple times. If `x` is not found, return -1.
"""

def binary_search(arr, x):
    left_index = 0
    right_index = len(arr) - 1

    # Store the indexes of start and end range
    start = -1
    end = -1

    # First binary search to find first occurrence
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2 

        if arr[mid_index] == x:
            start = mid_index
            # Do not break after we find, keep looking on the left (lower indices)
            right_index = mid_index - 1
        elif arr[mid_index] < x:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    if start == -1:
      # Element not found
      return -1

    left_index = 0
    right_index = len(arr) - 1

    # Second binary search to find last occurrence
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2 

        if arr[mid_index] == x:
            end = mid_index
            # Do not break after we find, keep looking on the right (higher indices)
            left_index = mid_index + 1
        elif arr[mid_index] < x:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return start, end