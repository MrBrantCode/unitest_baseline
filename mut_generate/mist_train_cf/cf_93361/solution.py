"""
QUESTION:
Create a function named find_longest_increasing_subarray that takes an array of positive integers as input. The function should return the longest continuous increasing subarray with at least three elements. If multiple subarrays have the same maximum length, any of them can be returned. The function should return an empty subarray if no such subarray exists.
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