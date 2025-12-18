"""
QUESTION:
Write a function `is_symmetric(matrix)` that calculates the transpose of the given matrix and checks if the matrix is symmetric. The function should take a 2D list `matrix` as input and return a boolean value indicating whether the matrix is symmetric. The function should have a time complexity of O(mn) and a space complexity of O(mn), where m is the number of rows and n is the number of columns in the matrix.
"""

def is_symmetric(matrix):
    """
    Checks if a given matrix is symmetric.

    Args:
        matrix (list of lists): A 2D list representing the matrix.

    Returns:
        bool: True if the matrix is symmetric, False otherwise.
    """
    # Get the number of rows and columns
    m = len(matrix)
    n = len(matrix[0])
    
    # Check if the matrix is square
    if m != n:
        return False
    
    # Iterate over the elements of the matrix
    for i in range(m):
        for j in range(n):
            # If the element is not equal to its mirrored element, return False
            if matrix[i][j] != matrix[j][i]:
                return False
    
    # If all elements are equal to their mirrored elements, return True
    return True