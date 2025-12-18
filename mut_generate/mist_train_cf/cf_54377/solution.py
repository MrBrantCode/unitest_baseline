"""
QUESTION:
Create a function `calc_diag_averages(matrix)` that calculates the sum of the elements in the primary and secondary diagonals of a given square 2D list `matrix` and their respective averages. The function should return four values: the sum of the primary diagonal, the sum of the secondary diagonal, the average of the primary diagonal, and the average of the secondary diagonal.
"""

def calc_diag_averages(matrix):
    len_matrix = len(matrix)
    primary_diag_sum = sum(matrix[i][i] for i in range(len_matrix))
    secondary_diag_sum = sum(matrix[i][len_matrix-i-1] for i in range(len_matrix))

    primary_diag_avg = primary_diag_sum/len_matrix
    secondary_diag_avg = secondary_diag_sum/len_matrix
    
    return primary_diag_sum, secondary_diag_sum, primary_diag_avg, secondary_diag_avg