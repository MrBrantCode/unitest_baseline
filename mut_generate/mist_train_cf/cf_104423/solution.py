"""
QUESTION:
Write a function `cumulative_sum_if` that takes an array of integers as input. Replace each value in the array with its cumulative sum if the value is greater than 0 and less than 10. Otherwise, keep the original value. Return the maximum value in the modified array.
"""

def cumulative_sum_if(arr):
    """
    This function takes an array of integers, replaces each value with its cumulative sum 
    if the value is greater than 0 and less than 10, and returns the maximum value.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The maximum value in the modified array.
    """
    cumulative_sum = 0
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] < 10:
            cumulative_sum += arr[i]
            arr[i] = cumulative_sum
    return max(arr)