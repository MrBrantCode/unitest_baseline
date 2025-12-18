"""
QUESTION:
Create a function called `count_and_sum` that takes an array of integers as input. The function should return a tuple containing the count of elements that are even, greater than 10, and divisible by 3, as well as the sum of these elements.
"""

def count_and_sum(arr):
    """
    Returns a tuple containing the count of elements in the array that are even, greater than 10, and divisible by 3,
    as well as the sum of these elements.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the count and sum of the elements that meet the specified conditions.
    """
    count = 0
    total_sum = 0  # Renamed variable to avoid shadowing built-in 'sum' function
    for num in arr:
        if num % 2 == 0 and num > 10 and num % 3 == 0:
            count += 1
            total_sum += num
    return count, total_sum