"""
QUESTION:
Write a function `find_longest_increasing_subarray` that takes an array of positive integers as input and returns the longest continuous increasing subarray containing at least three elements. The function should return the subarray itself, not just its length.
"""

def find_longest_increasing_subarray(arr):
    max_len = 0
    start_index = -1
    current_len = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_len += 1
        else:
            if current_len >= 3:
                if current_len > max_len:
                    max_len = current_len
                    start_index = i - current_len
            current_len = 1

    if current_len >= 3:
        if current_len > max_len:
            max_len = current_len
            start_index = len(arr) - current_len

    return arr[start_index: start_index + max_len]