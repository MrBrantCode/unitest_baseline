"""
QUESTION:
Create a function named `generate_squared_array` that takes two parameters, `start` and `end`, representing the start and end points of a range of integers (exclusive of the end point). The function should return an array containing the squares of these integers. The function should not include any default values for the start and end points, as they will be provided dynamically as user inputs.
"""

def generate_squared_array(start, end):
    """
    This function generates an array containing the squares of integers 
    within a specified range (exclusive of the end point).

    Args:
        start (int): The start point of the range.
        end (int): The end point of the range.

    Returns:
        list: A list of squared integers within the specified range.
    """
    return [i**2 for i in range(start, end)]