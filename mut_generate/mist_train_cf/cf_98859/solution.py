"""
QUESTION:
Write a Python function named `complete_matrix` that takes a square matrix as input, completes the matrix with the sum of each row, and returns the new matrix formatted in LaTeX. The function should handle cases where the input matrix is not square or contains non-numeric values, and return an error message in such cases.
"""

import numpy as np

def complete_matrix(matrix):
    try:
        matrix = np.array(matrix, dtype=float)
    except ValueError:
        return "Error: Matrix contains non-numeric values."
    if matrix.shape[0] != matrix.shape[1]:
        return "Error: Matrix is not square."
    row_sums = np.sum(matrix, axis=1)
    new_matrix = np.hstack((matrix, row_sums.reshape(-1, 1)))
    latex_matrix = "\\begin{tabular}{|" + "c|"*new_matrix.shape[1] + "}\n\\hline\n"
    for i in range(new_matrix.shape[0]):
        row = " & ".join([str(round(x, 2)) for x in new_matrix[i]])
        latex_matrix += row + " \\\\ \\hline\n"
    latex_matrix += "\\end{tabular}"
    return latex_matrix