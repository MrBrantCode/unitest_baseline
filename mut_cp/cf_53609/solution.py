"""
ORIGINAL QUESTION:
Construct a function `get_diagonal_sums` that takes a 2D array (square matrix) as input and returns a list containing the sums of its main and secondary diagonals. The main diagonal runs from the top left to the bottom right, and the secondary diagonal runs from the top right to the bottom left.
"""

def get_diagonal_sums(matrix):
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    matrix_size = len(matrix)
    
    for i in range(matrix_size):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][matrix_size - i - 1]
        
    return [main_diagonal_sum, secondary_diagonal_sum]