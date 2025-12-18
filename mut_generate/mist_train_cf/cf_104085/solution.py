"""
QUESTION:
Write a function named `sum_of_squares_divisible_by_three` that calculates the sum of the squares of the numbers in a given list that are divisible by 3. The input is a list of integers, and the output should be an integer representing the sum.
"""

def sum_of_squares_divisible_by_three(numbers):
    """
    This function calculates the sum of the squares of the numbers in a given list that are divisible by 3.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the squares of the numbers divisible by 3.
    """
    return sum([n ** 2 for n in numbers if n % 3 == 0])