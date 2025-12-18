"""
QUESTION:
Write a function named `find_numbers` that takes two parameters: a string representing a ratio of numbers separated by colons and a total sum of the numbers. The function should calculate and return a list of numbers that are in the given ratio and sum up to the total sum.
"""

def find_numbers(ratio, total_sum):
    """
    Calculate and return a list of numbers that are in the given ratio and sum up to the total sum.

    Args:
        ratio (str): A string representing a ratio of numbers separated by colons.
        total_sum (int): The total sum of the numbers.

    Returns:
        list: A list of numbers that are in the given ratio and sum up to the total sum.
    """

    # Convert the ratio to a list of integers
    ratio_list = [int(i) for i in ratio.split(':')]

    # Calculate the sum of the ratio
    ratio_sum = sum(ratio_list)

    # Calculate the value of 1 part in the ratio
    part_value = total_sum / ratio_sum

    # Calculate the value of each number
    numbers = [part * part_value for part in ratio_list]

    return numbers