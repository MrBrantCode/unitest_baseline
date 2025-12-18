"""
QUESTION:
Find the total sum of internal angles (in degrees) in an n-sided simple polygon. N will be greater than 2.
"""

def calculate_internal_angles_sum(n: int) -> int:
    """
    Calculate the total sum of internal angles in an n-sided simple polygon.

    Parameters:
    n (int): The number of sides in the polygon (n > 2).

    Returns:
    int: The total sum of internal angles in degrees.
    """
    return 180 * (n - 2)