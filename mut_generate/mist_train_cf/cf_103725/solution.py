"""
QUESTION:
Write a function named `sum_first_three_unique` that takes a list of integers as input and returns the sum of the first 3 unique numbers in the list. If there are less than 3 unique numbers in the list, return the sum of all unique numbers.
"""

def sum_first_three_unique(numbers):
    """
    Calculate the sum of the first 3 unique numbers in a list.
    
    If there are less than 3 unique numbers in the list, 
    return the sum of all unique numbers.
    
    Args:
    numbers (list): A list of integers.
    
    Returns:
    int: The sum of the first 3 unique numbers.
    """
    unique_numbers = list(dict.fromkeys(numbers))
    return sum(unique_numbers[:3]) if len(unique_numbers) >= 3 else sum(unique_numbers)