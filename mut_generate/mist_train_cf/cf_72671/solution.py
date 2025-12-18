"""
QUESTION:
Implement a function `binary_search` that performs a binary search on a generally increasing sequence (i.e., it can have equal values next to each other) to find the first occurrence of a target value. The function should take two parameters: `input_array` and `target`. The sequence is 0-indexed and the function should return the index of the first occurrence of the target value. If the target value does not exist in the sequence, the function should return -1.
"""

def binary_search(input_array, target):
    left, right = 0, len(input_array) - 1
    result = -1  
    while left <= right:
        middle = left + (right - left) // 2
        if input_array[middle] == target:
            result = middle
            right = middle - 1
        elif input_array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return result