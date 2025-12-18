"""
QUESTION:
Write a function named `find_max_sum` that takes an array of non-negative integers and an upper limit value as input, and returns the maximum sum of the array elements without exceeding the limit. The function should assume that the input array does not contain any negative numbers.
"""

def find_max_sum(array, limit):
    """
    This function calculates the maximum sum of array elements without exceeding the limit.

    Args:
    array (list): A list of non-negative integers.
    limit (int): The upper limit of the sum.

    Returns:
    int: The maximum sum of array elements without exceeding the limit.
    """
    array.sort()
    total = 0
    for num in array:
        if total + num <= limit:
            total += num
        else:
            break
    return total