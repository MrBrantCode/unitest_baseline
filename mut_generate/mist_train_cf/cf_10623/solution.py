"""
QUESTION:
Create a function named `extract_even_numbers` that takes a list of integers as input. The function should return a new list containing only the even numbers that are not divisible by 3, in descending order.
"""

def extract_even_numbers(numbers):
    """
    This function takes a list of integers, filters out the even numbers that are not divisible by 3, 
    and returns them in descending order.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A list of even numbers not divisible by 3 in descending order.
    """
    return [num for num in sorted(numbers, reverse=True) if num % 2 == 0 and num % 3 != 0]