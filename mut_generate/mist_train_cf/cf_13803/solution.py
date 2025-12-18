"""
QUESTION:
Write a function called `max_subarray_sum` that takes an array of integers as input and returns a tuple containing the maximum subarray sum and the start and end indices of the subarray with the maximum sum. The function should have a time complexity of O(n) and should not use any extra space other than a constant amount of space for variables.
"""

def max_subarray_sum(arr):
    """
    Returns a tuple containing the maximum subarray sum and the start and end indices of the subarray with the maximum sum.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the maximum subarray sum and the start and end indices.
    """
    max_sum = float('-inf')
    current_sum = 0
    start_index = 0
    max_start_index = 0
    max_end_index = 0

    for i, num in enumerate(arr):
        if current_sum <= 0:
            current_sum = num
            start_index = i
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = start_index
            max_end_index = i

    return max_sum, max_start_index, max_end_index