"""
QUESTION:
Write a function `max_pyramid_sum` that calculates the maximal cumulative total from the apex to the base of a pyramid. The function should take a 2D list `triangle` representing the pyramid as input, where each sublist represents a row of the pyramid. The function should return the maximal cumulative total. The function should use a dynamic programming approach, and it should not use any recursive calls or loops with a time complexity higher than O(n^2), where n is the number of rows in the pyramid.
"""

def max_pyramid_sum(triangle):
    """
    Calculate the maximal cumulative total from the apex to the base of a pyramid.

    Args:
    triangle (list): A 2D list representing the pyramid.

    Returns:
    int: The maximal cumulative total.

    """
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max( triangle[i+1][j], triangle[i+1][j+1] )
    return triangle[0][0]