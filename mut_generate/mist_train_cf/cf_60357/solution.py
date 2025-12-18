"""
QUESTION:
Write a function called `multi_dimensional_mul` that calculates the collective multiplication of elements in a given tri-dimensional matrix. The input matrix is a list of lists of lists of integers, and the function should return the product of all elements in the matrix.
"""

def multi_dimensional_mul(arr):
    """
    This function calculates the collective multiplication of elements in a given tri-dimensional matrix.
    
    Parameters:
    arr (list of lists of lists of integers): The input matrix
    
    Returns:
    int: The product of all elements in the matrix
    """
    mul = 1
    for element1 in arr:
        for element2 in element1:
            for element3 in element2:
                mul *= element3
    return mul