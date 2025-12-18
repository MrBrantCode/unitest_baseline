"""
QUESTION:
Create a function called `filter_divisible_numbers` that takes a list of numbers as input. The function should return a new list containing only the numbers from the original list that are not divisible by any number in the range from 2 to the square root of the number.
"""

import math

def filter_divisible_numbers(numbers):
    """
    This function filters out numbers that are not divisible by any number in the range from 2 to the square root of the number.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A new list containing only the numbers from the original list that are not divisible by any number in the range from 2 to the square root of the number.
    """
    filtered_list = []
    for number in numbers:
        is_divisible = False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_divisible = True
                break
        if not is_divisible:
            filtered_list.append(number)
    return filtered_list