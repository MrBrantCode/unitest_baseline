"""
QUESTION:
Write a function named `transpose_matrix` that takes a 2D list `matrix` as input, transposes the matrix, and handles edge cases such as uneven dimensions or null values within the matrix. The function should have the least possible time complexity.
"""

def transpose_matrix(matrix):
    try:
        transposed_matrix = [list(i) for i in zip(*matrix)]
        return transposed_matrix

    except TypeError as e:
        print(f"An error occurred: {e}")