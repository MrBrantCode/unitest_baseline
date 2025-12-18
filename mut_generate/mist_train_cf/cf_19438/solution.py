"""
QUESTION:
Construct a function construct_array(M, N) that creates a 2-dimensional array of size MxN. The array should be filled with ones, except for elements where the sum of their row index (0-based) and column index is odd, in which case the value should be 0.
"""

def construct_array(M, N):
    """
    Creates a 2-dimensional array of size MxN. 
    The array is filled with ones, except for elements where the sum of their row index (0-based) and column index is odd, in which case the value is 0.

    Parameters:
    M (int): The number of rows in the array.
    N (int): The number of columns in the array.

    Returns:
    list: A 2-dimensional array of size MxN.
    """
    return [[1 if (i + j) % 2 == 0 else 0 for j in range(N)] for i in range(M)]