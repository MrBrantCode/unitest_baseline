"""
QUESTION:
Create a function `calculate_average` that takes a 2D array (matrix) as input, calculates the average of each row, and returns the row number (0-indexed) and its corresponding average value with the highest average. The function should not take any additional parameters besides the matrix.
"""

def calculate_average(matrix):
    """
    This function calculates the average of each row in a given 2D array and returns the row number (0-indexed) and its corresponding average value with the highest average.

    Args:
        matrix (list): A 2D array of numbers.

    Returns:
        tuple: A tuple containing the row number (0-indexed) and the corresponding average value with the highest average.
    """
    row_averages = [sum(row) / len(row) for row in matrix]
    max_average = max(row_averages)
    max_index = row_averages.index(max_average)
    return max_index, max_average