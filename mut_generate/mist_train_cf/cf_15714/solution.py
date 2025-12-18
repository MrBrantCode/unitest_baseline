"""
QUESTION:
Create a function named `calculate_surface_area()` that takes the length, width, and height of a triangular prism as input and returns its surface area. The formula for the surface area is base area plus two times the side area, where base area is half of length times width and side area is length times height plus width times height. 

The function should not handle user inputs directly, but rather assume that the inputs are valid.
"""

def calculate_surface_area(length, width, height):
    """
    Calculate the surface area of a triangular prism.

    Parameters:
    length (float): The length of the triangular prism.
    width (float): The width of the triangular prism.
    height (float): The height of the triangular prism.

    Returns:
    float: The surface area of the triangular prism.
    """
    base_area = (length * width) / 2
    side_area = length * height + width * height
    surface_area = base_area + 2 * side_area
    return surface_area