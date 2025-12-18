"""
QUESTION:
Write a function named `count_and_sum` that takes an array of integers as input and returns a tuple containing the count of elements that are even, greater than 10, and divisible by 3, along with their sum. The array can contain negative numbers.
"""

def count_and_sum(arr):
    """
    This function takes an array of integers as input and returns a tuple containing 
    the count of elements that are even, greater than 10, and divisible by 3, 
    along with their sum.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the count and sum of the elements that meet the conditions.
    """
    count = 0
    total_sum = 0

    for num in arr:
        if num % 2 == 0 and num > 10 and num % 3 == 0:
            count += 1
            total_sum += num

    return count, total_sum