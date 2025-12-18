"""
QUESTION:
Write a function named `find_divisible_numbers` that takes a list of integers as input and returns a list of numbers that are divisible by both 3 and 5, have a remainder of 2 when divided by 7, and are greater than 10. The output list should be sorted in descending order.
"""

def find_divisible_numbers(lst):
    """
    Returns a list of numbers from the input list that are divisible by both 3 and 5, 
    have a remainder of 2 when divided by 7, and are greater than 10. 
    The output list is sorted in descending order.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A list of integers satisfying the conditions.
    """
    return sorted([num for num in lst if num % 3 == 0 and num % 5 == 0 and num > 10 and num % 7 == 2], reverse=True)