"""
QUESTION:
Implement a function named `create_sparse_matrix` that represents a sparse matrix using a suitable data structure, considering it will handle thousands of columns and rows.
"""

def create_sparse_matrix(matrix):
    """
    This function represents a sparse matrix using a dictionary of dictionaries.
    
    Args:
        matrix (list): A 2D list representing the sparse matrix.
        
    Returns:
        dict: A dictionary of dictionaries representing the sparse matrix.
    """
    
    sparse_matrix = {}
    for i, row in enumerate(matrix):
        sparse_row = {}
        for j, val in enumerate(row):
            if val != 0:
                sparse_row[j] = val
        if sparse_row:
            sparse_matrix[i] = sparse_row
    return sparse_matrix