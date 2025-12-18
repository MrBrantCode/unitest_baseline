"""
QUESTION:
Write a function named `matrix_sum` that calculates the maximum possible sum of matrix elements, with the condition that none of the chosen elements are from the same row or column. 

The function takes a 2D list of integers as input, representing the matrix, and returns the maximum possible sum of its elements. The matrix can be of any size, but it must be rectangular (i.e., all rows must have the same number of columns). The function should not modify the input matrix. 

The goal is to maximize the sum by selecting the largest possible numbers from each row, while avoiding numbers from the same column.
"""

def matrix_sum(matrix):
    """
    Calculate the maximum possible sum of matrix elements, with the condition that none of the chosen elements are from the same row or column.

    Args:
    matrix (list): A 2D list of integers representing the matrix.

    Returns:
    int: The maximum possible sum of matrix elements.
    """
    # Sort the matrix in descending order for each row
    sorted_matrix = [sorted(row, reverse=True) for row in matrix]

    used_cols = set()
    final_sum = 0

    for row_index, row in enumerate(sorted_matrix):
        for element in row:
            col_index = matrix[row_index].index(element)
            if col_index not in used_cols:
                final_sum += element
                used_cols.add(col_index)
                break

    return final_sum