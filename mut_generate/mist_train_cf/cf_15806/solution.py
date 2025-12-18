"""
QUESTION:
Write a function `sum_until_limit` that calculates the sum of integers from 0 to a given limit (inclusive) until the sum reaches or exceeds a specified threshold. The function should take two parameters: `limit` and `threshold`, where `limit` is the upper bound of the integers to be summed and `threshold` is the maximum sum. The function should return the final sum.
"""

def sum_until_limit(limit, threshold):
    """
    Calculate the sum of integers from 0 to a given limit (inclusive) until the sum reaches or exceeds a specified threshold.

    Args:
        limit (int): The upper bound of the integers to be summed.
        threshold (int): The maximum sum.

    Returns:
        int: The final sum.
    """
    total_sum = 0
    for i in range(limit + 1):
        if total_sum + i > threshold:
            break
        total_sum += i
    return total_sum