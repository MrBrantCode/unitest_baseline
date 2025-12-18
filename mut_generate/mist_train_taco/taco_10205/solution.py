"""
QUESTION:
problem

Given the lengths of $ 2 $ sides that are not the hypotenuse of a right triangle, $ A $ and $ B $. The side of length $ A $ overlaps the $ x $ axis, and the side of length $ B $ overlaps the $ y $ axis.

Do the following:

1. Rotate the triangle around the $ x $ axis.
2. Rotate the shape created by performing the operation $ 1 $ around the $ y $ axis.



Perform the operation $ 2 $ to find the volume of the created figure.



output

Output the volume of the figure. Also, output a line break at the end. Absolute or relative errors less than $ 0.000001 $ are allowed.

Example

Input

1 2


Output

33.510322
"""

import math

def calculate_rotated_volume(a: float, b: float) -> float:
    """
    Calculate the volume of the figure created by rotating a right triangle around the x and y axes.

    Parameters:
    a (float): The length of the side overlapping the x-axis.
    b (float): The length of the side overlapping the y-axis.

    Returns:
    float: The volume of the figure.
    """
    # Volume calculation based on the given operations
    volume = b ** 3 * math.pi * (4 / 3)
    return volume