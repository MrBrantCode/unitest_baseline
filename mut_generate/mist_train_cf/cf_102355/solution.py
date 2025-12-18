"""
QUESTION:
Write a function named `remove_divisible_by_2_and_3` that takes a list of integers as input, removes all numbers that are divisible by both 2 and 3, and returns the remaining numbers in descending order.
"""

def remove_divisible_by_2_and_3(numbers_list):
    """
    Removes all numbers that are divisible by both 2 and 3 from the input list and returns the remaining numbers in descending order.

    Args:
        numbers_list (list): A list of integers.

    Returns:
        list: The input list with numbers divisible by both 2 and 3 removed, sorted in descending order.
    """
    return sorted([num for num in numbers_list if num % 2 != 0 or num % 3 != 0], reverse=True)