"""
QUESTION:
Create a program that draws an equilateral triangle with a specified side length using the turtle module. The program should also draw a smaller, inverted equilateral triangle inside the larger triangle. The drawing should be able to adjust dynamically to the size of the canvas. Additionally, implement a function called `triangle_area` that calculates the area of an equilateral triangle given its side length. The function should use the formula `(math.sqrt(3) / 4) * (side_length ** 2)`. The program should output the areas of the two triangles to the console.
"""

import math

def triangle_area(side_length):
    """
    Calculate the area of an equilateral triangle given its side length.

    Args:
        side_length (float): The length of the side of the equilateral triangle.

    Returns:
        float: The area of the equilateral triangle.
    """
    return (math.sqrt(3) / 4) * (side_length ** 2)