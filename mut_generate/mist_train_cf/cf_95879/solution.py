"""
QUESTION:
Create a function `sum_numbers_in_array` that takes a 2D list of mixed data types as input, where each sublist contains at least 3 elements. The function should sum up all the integers in the list that are greater than or equal to 5, ignore non-integer elements, and return the result rounded to the nearest whole number.
"""

import math

def sum_numbers_in_array(array):
    """
    This function takes a 2D list of mixed data types, sums up all the integers 
    in the list that are greater than or equal to 5, ignores non-integer elements, 
    and returns the result rounded to the nearest whole number.

    Args:
        array (list): A 2D list of mixed data types.

    Returns:
        int: The sum of integers in the array that are greater than or equal to 5, rounded to the nearest whole number.
    """
    sum_of_numbers = 0
    for sublist in array:
        for element in sublist:
            if isinstance(element, int) and element >= 5:
                sum_of_numbers += element

    return round(sum_of_numbers)