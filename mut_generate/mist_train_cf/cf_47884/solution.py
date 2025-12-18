"""
QUESTION:
Given a triangular pyramid of integers, determine the maximal cumulative total from the apex to the base by moving to adjacent numbers in the next row. Implement a function, `max_pyramid_sum`, that takes a 2D list of integers representing the pyramid as input and returns the maximum cumulative total. Use dynamic programming to efficiently compute the solution.
"""

def max_pyramid_sum(pyramid):
    """
    This function calculates the maximum cumulative total from the apex to the base 
    of a triangular pyramid of integers by moving to adjacent numbers in the next row.
    
    Args:
    pyramid (list of lists): A 2D list of integers representing the pyramid.

    Returns:
    int: The maximum cumulative total.
    """
    for i in range(len(pyramid) - 2, -1, -1):
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
    return pyramid[0][0]