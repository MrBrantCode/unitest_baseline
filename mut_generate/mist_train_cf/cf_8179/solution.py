"""
QUESTION:
Write a function `find_highest_number` that takes a list of integers as input and returns the highest number greater than 100. The function should ignore any negative numbers in the list and only consider positive numbers. The input list can contain at most 10000 elements.
"""

def find_highest_number(numbers):
    """
    This function takes a list of integers as input, ignores any negative numbers, 
    and returns the highest number greater than 100.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The highest number greater than 100. If no such number exists, it returns None.
    """
    positive_numbers = [num for num in numbers if num > 0]
    numbers_greater_than_100 = [num for num in positive_numbers if num > 100]
    
    if numbers_greater_than_100:
        return max(numbers_greater_than_100)
    else:
        return None