"""
QUESTION:
Create a function named `check_conditions` that takes a list of integers as input. The function must return the sum of each element squared and multiplied by 2, as well as the list of squared and multiplied elements if the following conditions are met: the sum of the squared and multiplied elements is greater than 100, and all the squared elements (before multiplication by 2) are odd numbers. If the conditions are not met, return a message stating that the conditions are not satisfied.
"""

def check_conditions(numbers):
    """
    This function calculates the sum of each element squared and multiplied by 2, 
    and returns the sum along with the list of squared and multiplied elements 
    if the sum is greater than 100 and all the squared elements are odd numbers.

    Args:
    numbers (list): A list of integers.

    Returns:
    tuple: A tuple containing the sum of squared and multiplied elements, 
           the list of squared and multiplied elements, or a message if conditions are not met.
    """

    sum_squared_multiplied = sum(num ** 2 * 2 for num in numbers)
    squared_multiplied_elements = [num ** 2 * 2 for num in numbers if (num ** 2) % 2 == 1]

    if sum_squared_multiplied > 100 and len(squared_multiplied_elements) == len(numbers):
        return sum_squared_multiplied, squared_multiplied_elements
    else:
        return "The conditions are not satisfied."