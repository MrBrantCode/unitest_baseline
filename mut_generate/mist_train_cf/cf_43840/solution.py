"""
QUESTION:
Write a function `cube_sum_square_product` that takes a list of integers as input. The function should return a tuple of two integers. The first integer in the tuple should be the sum of the cubes of all numbers in the input list. The second integer should be the product of the squares of all numbers in the input list. If the input list is empty, the function should return (0, 1).
"""

def cube_sum_square_product(numbers):
    """
    Calculate the sum of cubes and product of squares of numbers in a list.

    Args:
    numbers (list): A list of integers.

    Returns:
    tuple: A tuple containing the sum of cubes and product of squares.
    """
    cube_sum = 0
    square_product = 1
    for num in numbers:
        cube_sum += num ** 3
        square_product *= num ** 2
    return cube_sum, square_product