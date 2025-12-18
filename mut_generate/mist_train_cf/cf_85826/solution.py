"""
QUESTION:
Write a function `calculate_sums(arr)` that calculates the sum of the elements and the sum of their squares in a given array. The function should include exception handling for non-numeric array elements, excluding them from the calculations.
"""

def calculate_sums(arr):
    """
    Calculate the sum of the elements and the sum of their squares in a given array.
    Non-numeric array elements are excluded from the calculations.

    Args:
        arr (list): A list of numbers and/or non-numeric elements.

    Returns:
        tuple: A tuple containing the sum of the elements and the sum of their squares.
    """

    sum_of_elements = 0
    sum_of_squares = 0

    for i in arr:
        try:
            sum_of_elements += i
            sum_of_squares += i*i
        except TypeError:
            print(f"'{i}' is not a number and excluded from operations")

    return sum_of_elements, sum_of_squares