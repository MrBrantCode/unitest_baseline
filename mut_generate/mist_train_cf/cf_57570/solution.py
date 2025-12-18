"""
QUESTION:
Write a function `calculate_sum_product_average` that takes a list of numbers as input and returns the sum, product, and average of the numbers without using any built-in sum or product functions. The function should use the accumulator pattern to calculate the sum and product, and then use these values to calculate the average. Assume that the input list is not empty and contains only numbers.
"""

def calculate_sum_product_average(numbers):
    """
    Calculate the sum, product, and average of a list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    tuple: A tuple containing the sum, product, and average of the numbers.
    """
    accumulator_sum = 0
    accumulator_product = 1

    for num in numbers:
        accumulator_sum += num
        accumulator_product *= num

    average = accumulator_sum / len(numbers)

    return accumulator_sum, accumulator_product, average