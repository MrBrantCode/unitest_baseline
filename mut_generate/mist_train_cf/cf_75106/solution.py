"""
QUESTION:
Write a function `most_common_output(matrix)` that takes a 3D matrix of ternary variables and returns the most common output after modifying each variable to 'Yes', 'No', or 'Maybe' based on its value (0, 1, or 2 respectively). If there is a tie for the most common value, return 'Tie'. The function should be optimized for large matrices.
"""

import numpy as np
from collections import Counter

def most_common_output(matrix):
    matrix = np.array(matrix)
    output_matrix = np.where(matrix==0, 'Yes',
                        np.where(matrix==1, 'No',
                                 'Maybe'))
    output_counts = Counter(output_matrix.flatten())
    common_values = output_counts.most_common(2)
    if len(common_values) > 1 and common_values[0][1] == common_values[1][1]:
        return 'Tie'
    else:
        return common_values[0][0]