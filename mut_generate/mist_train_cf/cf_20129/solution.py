"""
QUESTION:
Write a function called `maximal_square_area` that finds the area of the largest square sub-matrix composed of only '1s' in a given n x n matrix. The function should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def maximal_square_area(matrix):
    """
    Finds the area of the largest square sub-matrix composed of only '1s' in a given n x n matrix.

    Args:
        matrix (list): A 2D list of '1s' and '0s' representing the given matrix.

    Returns:
        int: The area of the largest square sub-matrix composed of only '1s'.
    """

    n = len(matrix)
    max_side_length = 0
    max_side_length_pos = (0,0)
    dp_matrix = [0] * n
    prev = 0

    for row in range(n):
        for column in range(n):
            if matrix[row][column] == '1':
                if column == 0:
                    dp_matrix[column] = 1
                else:
                    dp_matrix[column] = min(dp_matrix[column - 1], prev, dp_matrix[column]) + 1
                if dp_matrix[column] > max_side_length:
                    max_side_length = dp_matrix[column]
                    max_side_length_pos = (row - max_side_length + 1, column - max_side_length + 1)
                prev = dp_matrix[column]
            else:
                dp_matrix[column] = 0
                prev = dp_matrix[column - 1] if column > 0 else 0

    return max_side_length * max_side_length