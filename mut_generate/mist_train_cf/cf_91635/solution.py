"""
QUESTION:
Write a function `filter_divisible_numbers` that takes a list of integers as input and returns a list of numbers that are divisible by both 2 and 3, sorted in descending order.
"""

def filter_divisible_numbers(numbers):
    """
    Returns a list of numbers that are divisible by both 2 and 3, sorted in descending order.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: A list of numbers that are divisible by both 2 and 3, sorted in descending order.
    """
    return sorted([num for num in numbers if num % 2 == 0 and num % 3 == 0], reverse=True)