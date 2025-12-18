"""
QUESTION:
Write a function called `find_max_values` that takes a 2D list of integers as input and returns a list of maximum values, one from each row. The maximum value in each row must be greater than 100; if no such value exists in a row, return "None" for that row.
"""

def find_max_values(matrix):
    """
    This function takes a 2D list of integers as input and returns a list of maximum values, 
    one from each row. The maximum value in each row must be greater than 100; 
    if no such value exists in a row, return "None" for that row.

    Args:
        matrix (list): A 2D list of integers.

    Returns:
        list: A list of maximum values from each row.
    """
    result = []
    for row in matrix:
        maximum_value = max(row)
        if maximum_value > 100:
            result.append(maximum_value)
        else:
            result.append("None")
    return result