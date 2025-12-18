"""
QUESTION:
Write a function named `find_divisible_numbers` that takes a list of integers as input and returns a list of numbers that are divisible by both 3 and 5, and are greater than 10. The output list should be sorted in descending order.
"""

def find_divisible_numbers(numbers):
    """
    Returns a list of numbers that are divisible by both 3 and 5, and are greater than 10.
    The output list is sorted in descending order.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: A list of numbers that meet the specified conditions.
    """
    return sorted([num for num in numbers if num % 3 == 0 and num % 5 == 0 and num > 10], reverse=True)