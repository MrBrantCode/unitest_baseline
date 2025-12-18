"""
QUESTION:
Given an n x n matrix A, write a function `calculate_trace(A)` to calculate the trace of A, defined as the sum of the elements on the main diagonal. The matrix A is represented as a list of lists, where each inner list represents a row of the matrix.
"""

def calculate_trace(A):
    """
    Calculate the trace of a square matrix A.
    
    Args:
    A (list of lists): A square matrix represented as a list of lists.
    
    Returns:
    int: The sum of the elements on the main diagonal of the matrix.
    """
    return sum(A[i][i] for i in range(len(A)))