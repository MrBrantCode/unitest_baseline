"""
QUESTION:
Write a function named `find_highest_positive_number` that takes a list of integers as input, ignores any negative numbers, and returns the highest positive number in the list. If the list is empty or contains no positive numbers, return None.
"""

def find_highest_positive_number(numbers):
    """
    This function takes a list of integers, ignores any negative numbers, 
    and returns the highest positive number in the list. 
    If the list is empty or contains no positive numbers, return None.

    Args:
        numbers (list): A list of integers.

    Returns:
        int or None: The highest positive number in the list or None if not found.
    """
    positive_numbers = [num for num in numbers if num > 0]
    return max(positive_numbers) if positive_numbers else None