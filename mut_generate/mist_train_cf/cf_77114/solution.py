"""
QUESTION:
Write a function `calculate_cubes_and_sum` that takes an array of numbers as input and returns the total sum of the cube of each element in the array.
"""

def calculate_cubes_and_sum(numbers):
    """
    This function calculates the total sum of the cube of each element in the input array.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The total sum of the cube of each element in the array.
    """
    total_sum = sum(num ** 3 for num in numbers)
    return total_sum