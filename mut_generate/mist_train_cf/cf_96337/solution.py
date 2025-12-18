"""
QUESTION:
Write a function `calculate_modified_sum` that takes an array of integers as input and returns the sum of the numbers in the array, excluding any numbers that are divisible by 3 or 5, unless they are divisible by both 3 and 5.
"""

def calculate_modified_sum(numbers):
    """
    This function calculates the sum of numbers in an array, excluding numbers 
    divisible by 3 or 5 unless they are divisible by both 3 and 5.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The modified sum of the numbers in the array.
    """
    total_sum = 0
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            total_sum += num
        elif num % 3 != 0 and num % 5 != 0:
            total_sum += num
    return total_sum