"""
QUESTION:
Create a function named `filter_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers. Use a lambda expression within the function to filter out even numbers.
"""

def filter_odd_numbers(numbers):
    """
    This function takes a list of integers as input, filters out even numbers using a lambda expression, 
    and returns a new list containing only the odd numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of odd integers.
    """
    return list(filter(lambda x: x % 2 != 0, numbers))