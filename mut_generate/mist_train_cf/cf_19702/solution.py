"""
QUESTION:
Write a function called 'sum_of_interior_angles' that calculates the sum of the interior angles of a regular polygon. The function should take the number of sides of the polygon as input and return the sum of the interior angles in degrees.
"""

def sum_of_interior_angles(n):
    """
    Calculate the sum of the interior angles of a regular polygon.

    Parameters:
    n (int): The number of sides of the polygon.

    Returns:
    int: The sum of the interior angles in degrees.
    """
    return (n - 2) * 180