"""
QUESTION:
Write a function named `find_max_and_second_max` that finds the maximum value and its index, and the second maximum value in a given list of integers with a single traversal. If the maximum value appears multiple times, consider the first occurrence as the maximum. Similarly, if the second maximum value appears multiple times, consider the first occurrence as the second maximum. The function should return the maximum value, its index, the second maximum value, and its index. If there is no second maximum value (i.e., all elements are the same), return the maximum value, its index, the minimum possible integer value, and -1 as the second maximum value and its index respectively.
"""

def find_max_and_second_max(arr):
    max_val = float('-inf')
    second_max_val = float('-inf')
    max_idx = -1
    second_max_idx = -1

    for i, ele in enumerate(arr):
        if ele > max_val:
            second_max_val = max_val
            second_max_idx = max_idx
            max_val = ele
            max_idx = i
        elif ele > second_max_val and ele != max_val:
            second_max_val = ele
            second_max_idx = i

    return max_val, max_idx, second_max_val, second_max_idx