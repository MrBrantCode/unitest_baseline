"""
QUESTION:
Write a function `sum_of_first_three` that takes a list of integers as input, filters out the numbers that can be perfectly divided by 2, sorts the remaining numbers in descending order, and returns the sum of the first three numbers.
"""

def sum_of_first_three(numbers):
    """
    This function takes a list of integers, filters out the numbers that can be perfectly divided by 2, 
    sorts the remaining numbers in descending order, and returns the sum of the first three numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the first three numbers.
    """
    # Filter numbers that can be perfectly divided by 2 and sort in descending order
    filtered_numbers = sorted([n for n in numbers if n % 2 == 0], reverse=True)
    
    # Sum of first three numbers
    return sum(filtered_numbers[:3])