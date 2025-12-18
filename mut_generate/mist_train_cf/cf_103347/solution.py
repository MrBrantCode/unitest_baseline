"""
QUESTION:
Write a function named `sum_positive_numbers` that takes a list of numbers as input, skips any negative numbers, and calculates the sum of the remaining numbers using the `continue` keyword. The function should return the sum of the positive numbers. The input list can contain both positive and negative integers.
"""

def sum_positive_numbers(numbers):
    """
    This function calculates the sum of positive numbers in a given list.
    
    Args:
        numbers (list): A list of integers containing both positive and negative numbers.
    
    Returns:
        int: The sum of the positive numbers in the list.
    """
    sum_of_positive_numbers = 0
    for num in numbers:
        if num < 0:
            continue  # skip negative numbers
        sum_of_positive_numbers += num
    return sum_of_positive_numbers