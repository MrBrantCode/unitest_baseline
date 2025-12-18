"""
QUESTION:
Write a function named `sum_even_numbers` that uses a while loop to calculate the sum of all even numbers in a given list of integers. The function should return the sum of the even numbers. The input list can contain any number of integers, and the function should handle this variation.
"""

def sum_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in a given list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The sum of the even numbers.
    """
    index = 0
    sum_of_even = 0

    while index < len(numbers):
        if numbers[index] % 2 == 0:
            sum_of_even += numbers[index]
        index += 1

    return sum_of_even