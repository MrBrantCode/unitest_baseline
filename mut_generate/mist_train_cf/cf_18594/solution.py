"""
QUESTION:
Create a function `find_numbers` that takes a list of integers and two integers X and Z as input. The function should return a list of numbers from the input list that are greater than X and divisible by Z.
"""

def find_numbers(lst, x, z):
    """
    This function takes a list of integers and two integers X and Z as input.
    It returns a list of numbers from the input list that are greater than X and divisible by Z.

    Parameters:
    lst (list): A list of integers.
    x (int): The number to compare with.
    z (int): The divisor.

    Returns:
    list: A list of numbers that meet the conditions.
    """
    return [num for num in lst if num > x and num % z == 0]