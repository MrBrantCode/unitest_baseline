"""
QUESTION:
Write a function `calculate_rectangle_area` that takes two complex numbers `top_left` and `bottom_right` representing the coordinates of the top-left and bottom-right corners of a rectangle, and returns the area of the rectangle.
"""

def calculate_rectangle_area(top_left, bottom_right):
    """
    Calculate the area of a rectangle given its top-left and bottom-right corners.

    Args:
    top_left (complex): The complex number representing the top-left corner of the rectangle.
    bottom_right (complex): The complex number representing the bottom-right corner of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    # Calculate the length of the rectangle by subtracting the real parts of the coordinates
    length = bottom_right.real - top_left.real
    
    # Calculate the height of the rectangle by subtracting the imaginary parts of the coordinates
    height = top_left.imag - bottom_right.imag
    
    # Calculate the area of the rectangle by multiplying the length and the height
    area = abs(length * height)
    
    return area