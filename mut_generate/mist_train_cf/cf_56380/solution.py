"""
QUESTION:
Given a regular polygon with 'n' sides and a side length of 'a' units, find the side length of a second polygon constructed within the first such that the longest diagonals of the second shape coincide with the sides of the first shape. Assume 'n' is greater than 2. The solution should be generalized to handle any regular polygon with 'n' sides.
"""

import math

def entrance(n, a):
    """
    Calculate the side length of a second polygon constructed within the first such that 
    the longest diagonals of the second shape coincide with the sides of the first shape.

    Parameters:
    n (int): Number of sides of the regular polygon. It should be greater than 2.
    a (float): Length of each side of the regular polygon.

    Returns:
    float: Side length of the second polygon.
    """
    return 2 * a * math.cos(math.pi * (n - 2) / (2 * n))