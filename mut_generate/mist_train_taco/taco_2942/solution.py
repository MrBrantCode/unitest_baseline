"""
QUESTION:
Write a program which calculates the area and circumference of a circle for given radius r.

Constraints

* 0 < r < 10000

Input

A real number r is given.

Output

Print the area and circumference of the circle in a line. Put a single space between them. The output should not contain an absolute error greater than 10-5.

Examples

Input

2


Output

12.566371 12.566371


Input

3


Output

28.274334 18.849556
"""

import math

def calculate_circle_properties(radius: float) -> tuple:
    """
    Calculate the area and circumference of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    tuple: A tuple containing the area and circumference of the circle.
    """
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return (area, circumference)