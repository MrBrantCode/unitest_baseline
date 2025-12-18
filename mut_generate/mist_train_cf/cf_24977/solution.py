"""
QUESTION:
Find the largest sub-array in a given array with contiguous elements and its sum. Implement a function `largest_subarray_sum(array)` that takes an array of integers as input and returns a tuple containing the maximum sum and the start and end indices of the sub-array that yields this sum. The sub-array must have contiguous elements.
"""

def largest_subarray_sum(array):
    """
    Find the largest sub-array in a given array with contiguous elements and its sum.

    Args:
    array (list): A list of integers.

    Returns:
    tuple: A tuple containing the maximum sum and the start and end indices of the sub-array that yields this sum.
    """
    best_sum = 0
    current_sum = 0
    current_start_index = 0
    best_start_index = -1
    best_end_index = -1
    for i in range(len(array)):
        current_sum += array[i]
        if current_sum > best_sum:
            best_sum = current_sum
            best_start_index = current_start_index
            best_end_index = i
        if current_sum < 0:
            current_sum = 0
            current_start_index = i + 1
    return (best_sum, best_start_index, best_end_index)