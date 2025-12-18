"""
QUESTION:
Write a function `max_subarray_sum` that calculates the maximum sum of a subarray of length k within a given array of integers. The function should take two parameters: an array of integers and an integer k representing the length of the subarray. The function should return the maximum sum of a subarray of length k. The array can contain any integer values and k will be a positive integer less than or equal to the length of the array.
"""

def max_subarray_sum(nums, k):
    """
    This function calculates the maximum sum of a subarray of length k within a given array of integers.

    Args:
        nums (list): A list of integers.
        k (int): The length of the subarray.

    Returns:
        int: The maximum sum of a subarray of length k.
    """

    # Initialize the maximum sum and the current sum as negative infinity
    max_sum = float('-inf')
    current_sum = 0

    # Initialize the window start index
    window_start = 0

    # Iterate over the array
    for window_end in range(len(nums)):
        # Add the current element to the current sum
        current_sum += nums[window_end]

        # If the window size is greater than k, subtract the element at the window start index from the current sum and move the window start index forward
        if window_end >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[window_start]
            window_start += 1

    # Return the maximum sum
    return max_sum