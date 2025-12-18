"""
QUESTION:
Implement a function `sum_excluding_elements` that takes a 2D array as input and returns the sum of all elements that are greater than 5 and less than 15, excluding any elements that are divisible by both 2 and 3.
"""

def sum_excluding_elements(array):
    """
    This function takes a 2D array as input and returns the sum of all elements 
    that are greater than 5 and less than 15, excluding any elements that are 
    divisible by both 2 and 3.

    Args:
        array (list): A 2D list of integers.

    Returns:
        int: The sum of elements that meet the conditions.
    """
    sum = 0
    for row in array:
        for element in row:
            if 5 < element < 15 and not (element % 2 == 0 and element % 3 == 0):
                sum += element
    return sum