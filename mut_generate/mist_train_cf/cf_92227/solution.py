"""
QUESTION:
Create a function `calculate_average(matrix)` that takes a 2D array `matrix` as input and returns the row index with the highest average value along with its corresponding average. The row index should be 0-indexed. The input matrix will contain integers.
"""

def calculate_average(matrix):
    """
    Calculate the row index with the highest average value in a 2D matrix.

    Args:
        matrix (list): A 2D list of integers.

    Returns:
        tuple: A tuple containing the row index (0-indexed) and its corresponding average value.
    """
    row_averages = [sum(row) / len(row) for row in matrix]
    max_average = max(row_averages)
    max_index = row_averages.index(max_average)
    return max_index, max_average