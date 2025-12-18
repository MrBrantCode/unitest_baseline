"""
QUESTION:
Implement a function `normalize(matrix)` that takes a 2D list of integers `matrix` as input and returns the normalized matrix. The normalization rule is as follows: the highest absolute value in the matrix becomes 100 and the lowest absolute value becomes -100. If the matrix is empty or contains only zeros, the function should return the original matrix.
"""

def normalize(matrix):
    if not matrix or all(all(val == 0 for val in row) for row in matrix):
        return matrix  

    flat = [abs(val) for row in matrix for val in row]  
    max_val = max(flat)  

    if max_val == 0:
        return matrix  

    normalized_matrix = []
    for row in matrix:
        normalized_row = []
        for val in row:
            if val == 0:
                normalized_row.append(0)
            else:
                normalized_row.append(int(val / max_val * 100))  
        normalized_matrix.append(normalized_row)

    return normalized_matrix