"""
QUESTION:
Create a function called `sum_of_squared_deviations` that calculates the sum of the squared deviations between each integer in the input array and the arithmetic mean of the entire array. The input array will contain only integers. The function should return a float value.
"""

def sum_of_squared_deviations(array):
    """
    This function calculates the sum of the squared deviations between each integer in the input array and the arithmetic mean of the entire array.

    Parameters:
    array (list): A list of integers.

    Returns:
    float: The sum of the squared deviations.
    """
    mean = sum(array) / len(array)
    squared_deviations = [(i - mean)**2 for i in array]
    return sum(squared_deviations)