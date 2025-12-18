"""
QUESTION:
Create a function `find_longest_common_subarray(arr1, arr2)` that finds the longest common contiguous subarray between two integer arrays. The function should have a time complexity of O(n) and space complexity of O(1). The input arrays are sorted in ascending order.
"""

def find_longest_common_subarray(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    # Initialize variables for tracking the longest common subarray
    max_len = 0
    max_start = 0
    current_len = 0
    current_start = 0

    i, j = 0, 0

    while i < m and j < n:
        if arr1[i] == arr2[j]:
            if current_len == 0:
                current_start = i
            current_len += 1
            i += 1
            j += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start = current_start
            current_len = 0
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

    # Check if the last contiguous subarray is the longest
    if current_len > max_len:
        max_len = current_len
        max_start = current_start

    return arr1[max_start:max_start + max_len]