"""
QUESTION:
Create a function called `sum_divisible_by_4_and_5` that takes two parameters, `lower_bound` and `upper_bound`, and returns the sum of all numbers between `lower_bound` and `upper_bound` (inclusive) that are divisible by both 4 and 5.
"""

def sum_divisible_by_4_and_5(lower_bound, upper_bound):
    """
    Calculate the sum of all numbers between lower_bound and upper_bound (inclusive) 
    that are divisible by both 4 and 5.

    Args:
        lower_bound (int): The lower bound of the range.
        upper_bound (int): The upper bound of the range.

    Returns:
        int: The sum of all numbers in the range that are divisible by both 4 and 5.
    """
    return sum(num for num in range(lower_bound, upper_bound + 1) if num % 4 == 0 and num % 5 == 0)