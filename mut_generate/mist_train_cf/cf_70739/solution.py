"""
QUESTION:
Implement a function `get_paint_cost` that takes the width and height of a rectangle as input and returns the total cost of painting the rectangle, given that the cost of painting is $70 per unit area.
"""

def get_paint_cost(width, height):
    """
    Calculate the total cost of painting a rectangle.
    
    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    
    Returns:
    int: The total cost of painting the rectangle.
    """
    area = width * height
    return area * 70