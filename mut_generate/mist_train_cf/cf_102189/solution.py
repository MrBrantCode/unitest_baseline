"""
QUESTION:
Write a function named `calculate_shape_properties` that takes four parameters: `n`, `m`, `p`, and `q`, representing the length and width of a rectangle, and the base and height of a triangle, respectively. The function should return a tuple containing the total area and the perimeter of the combined shape. The rectangle has a length of `n` units and a width of `m` units, and the triangle has a base of `p` units and a height of `q` units, where `n`, `m`, `p`, and `q` are all positive integers.
"""

def calculate_shape_properties(n, m, p, q):
    """
    This function calculates the total area and perimeter of a combined shape.
    
    The shape consists of a rectangle with length n and width m, and a triangle with base p and height q.
    
    Parameters:
    n (int): The length of the rectangle.
    m (int): The width of the rectangle.
    p (int): The base of the triangle.
    q (int): The height of the triangle.
    
    Returns:
    tuple: A tuple containing the total area and perimeter of the combined shape.
    """
    # Calculate the area of the rectangle
    rectangle_area = n * m
    
    # Calculate the area of the triangle
    triangle_area = 0.5 * p * q
    
    # Calculate the total area
    total_area = rectangle_area + triangle_area
    
    # Calculate the perimeter of the rectangle
    rectangle_perimeter = 2 * (n + m)
    
    # Calculate the perimeter of the triangle using the Pythagorean theorem for the hypotenuse
    triangle_perimeter = p + 2 * ((p/2)**2 + q**2)**0.5
    
    # Calculate the total perimeter
    total_perimeter = rectangle_perimeter + triangle_perimeter
    
    # Return the total area and perimeter
    return total_area, total_perimeter