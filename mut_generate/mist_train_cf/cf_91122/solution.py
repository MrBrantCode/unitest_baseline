"""
QUESTION:
Create a function named `filter_and_sort` that takes a list of integers as input and returns a new list containing only the numbers divisible by both 3 and 4, sorted in descending order.
"""

def filter_and_sort(numbers):
    """
    Filters a list of numbers and returns a new list containing only the numbers 
    divisible by both 3 and 4, sorted in descending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of integers divisible by both 3 and 4, sorted in descending order.
    """
    return sorted([num for num in numbers if num % 3 == 0 and num % 4 == 0], reverse=True)