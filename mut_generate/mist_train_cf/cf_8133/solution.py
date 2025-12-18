"""
QUESTION:
Create a function `get_odd_numbers(lower_bound, upper_bound, include_divisible_by_3)` that takes three parameters: two integers `lower_bound` and `upper_bound` representing the range of numbers, and a string `include_divisible_by_3` that is either 'y' or 'n'. The function should return a list of odd numbers in the specified range, including or excluding numbers that are divisible by 3 based on the value of `include_divisible_by_3`. The function should assume that `lower_bound` is less than `upper_bound` and that the inputs are valid.
"""

def get_odd_numbers(lower_bound, upper_bound, include_divisible_by_3):
    """
    Returns a list of odd numbers in the specified range, including or excluding numbers that are divisible by 3 based on the value of include_divisible_by_3.

    Args:
        lower_bound (int): The lower bound of the range (inclusive).
        upper_bound (int): The upper bound of the range (inclusive).
        include_divisible_by_3 (str): 'y' to include numbers divisible by 3, 'n' to exclude them.

    Returns:
        list: A list of odd numbers in the specified range.
    """
    return [num for num in range(lower_bound, upper_bound + 1) if num % 2 != 0 and (include_divisible_by_3 == 'y' or num % 3 != 0)]