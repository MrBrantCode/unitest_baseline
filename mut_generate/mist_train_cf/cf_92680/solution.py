"""
QUESTION:
Create a function named `find_max_length` that takes a list of integers as input and returns the maximum length of a subarray where elements are in non-decreasing order. The function should be able to handle both positive and negative integers, and the input list should have at least 5 elements.
"""

def find_max_length(arr):
    max_length = 0
    current_length = 1

    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length