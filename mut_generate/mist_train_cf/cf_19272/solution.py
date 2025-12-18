"""
QUESTION:
Create a function `sum_positive_non_adjacent` that takes a list of integers as input. Calculate the sum of all the positive numbers in the list, ignoring any negative numbers that are adjacent to a positive number.
"""

def sum_positive_non_adjacent(numbers):
    """
    Calculate the sum of all the positive numbers in the list, 
    ignoring any negative numbers that are adjacent to a positive number.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of positive non-adjacent numbers.
    """
    total_sum = 0
    add_current = True
    for num in numbers:
        if num > 0:
            if add_current:
                total_sum += num
            add_current = False
        else:
            add_current = True
    return total_sum