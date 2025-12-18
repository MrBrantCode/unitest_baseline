"""
QUESTION:
Create a function `sum_of_interior_angles` that calculates the sum of the interior angles in a regular polygon with n sides, where n is an integer greater than or equal to 3. The function should take an integer n as input and return the sum of interior angles. The time complexity of the function should be O(1) and the space complexity should be O(1).
"""

def sum_of_interior_angles(n):
    """
    Calculate the sum of the interior angles in a regular polygon with n sides.
    
    Args:
    n (int): The number of sides in the polygon.
    
    Returns:
    int: The sum of interior angles in the polygon.
    """
    return (n - 2) * 180