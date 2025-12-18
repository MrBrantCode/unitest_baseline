"""
QUESTION:
Calculate the cumulative load-bearing exterior coverage of a 3D rectangular parallelepiped given its dimensions. Implement a function named `cumulative_load_bearing_exterior_coverage(length, width, height)` that takes the length, width, and height of the parallelepiped as arguments and returns the surface area. The dimensions are in centimeters.
"""

def cumulative_load_bearing_exterior_coverage(length, width, height):
    """
    Calculate the cumulative load-bearing exterior coverage of a 3D rectangular parallelepiped.

    Args:
        length (float): The length of the parallelepiped in centimeters.
        width (float): The width of the parallelepiped in centimeters.
        height (float): The height of the parallelepiped in centimeters.

    Returns:
        float: The surface area of the parallelepiped in square centimeters.
    """
    return 2 * (length * width + length * height + width * height)