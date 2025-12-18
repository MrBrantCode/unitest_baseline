"""
QUESTION:
Create a function named `create2DArray` that accepts two integers `n` and `m`, creates a 2D array of `n` rows and `m` columns, initializes all elements to zero, and returns the 2D array. The function should handle memory management to prevent memory leaks. Note that the input parameters `n` and `m` are integers representing the number of rows and columns of the 2D array, respectively.
"""

def create2DArray(n, m):
    """
    Creates a 2D array of n rows and m columns, initializes all elements to zero, 
    and returns the 2D array.
    
    Parameters:
    n (int): The number of rows in the 2D array.
    m (int): The number of columns in the 2D array.
    
    Returns:
    list: A 2D array of n rows and m columns with all elements initialized to zero.
    """
    return [[0 for _ in range(m)] for _ in range(n)]