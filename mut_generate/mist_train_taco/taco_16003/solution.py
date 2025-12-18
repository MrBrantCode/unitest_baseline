"""
QUESTION:
Determine the **area** of the largest square that can fit inside a circle with radius *r*.
"""

def calculate_largest_square_area(radius: float) -> float:
    """
    Calculate the area of the largest square that can fit inside a circle with the given radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the largest square that can fit inside the circle.
    """
    return 2 * radius ** 2