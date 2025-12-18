"""
QUESTION:
Create a function `get_even_cubed_numbers` that takes a list of integers as input and returns a list of even numbers that are divisible by 4, cubed, and sorted in descending order.
"""

def get_even_cubed_numbers(lst):
    """
    Returns a list of even numbers that are divisible by 4, cubed, and sorted in descending order.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A list of even numbers that are divisible by 4, cubed, and sorted in descending order.
    """
    return sorted([num**3 for num in lst if num % 2 == 0 and num % 4 == 0], reverse=True)