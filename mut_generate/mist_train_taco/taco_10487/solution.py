"""
QUESTION:
A triangle is called an equable triangle if its area equals its perimeter. Return `true`, if it is an equable triangle, else return `false`. You will be provided with the length of sides of the triangle. Happy Coding!
"""

def is_equable_triangle(a: float, b: float, c: float) -> bool:
    """
    Determines if a triangle is equable. A triangle is equable if its area equals its perimeter.

    Parameters:
    a (float): The length of the first side of the triangle.
    b (float): The length of the second side of the triangle.
    c (float): The length of the third side of the triangle.

    Returns:
    bool: True if the triangle is equable, False otherwise.
    """
    # Calculate the perimeter of the triangle
    perimeter = a + b + c
    
    # Calculate the semi-perimeter
    s = perimeter / 2
    
    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    # Check if the area equals the perimeter
    return area == perimeter