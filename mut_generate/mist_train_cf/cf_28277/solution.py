"""
QUESTION:
Create a `GeometricObject` class with methods `calculate_volume` and `calculate_surface_area` to calculate the volume and surface area of the geometric object based on its dimension and embedding manifold. The class should handle different dimensions (up to 3) correctly and return `None` for dimensions higher than 3. The formulas for volume and surface area calculation are as follows: 

- For 1-dimensional objects, volume and surface area are 0.
- For 2-dimensional objects (e.g., circle), volume is pi and surface area is 2 * pi.
- For 3-dimensional objects (e.g., sphere), volume is (4/3) * pi and surface area is 4 * pi.
"""

import math

def geometric_object_properties(dimension):
    """
    Calculate the volume and surface area of a geometric object based on its dimension.

    Args:
        dimension (int): The dimension of the geometric object.

    Returns:
        tuple: A tuple containing the volume and surface area of the geometric object.
    """
    if dimension == 1:
        return 0, 0  # Volume and surface area of a 1-dimensional object are 0
    elif dimension == 2:
        return math.pi, 2 * math.pi  # Volume and surface area of a 2-dimensional object (e.g., circle)
    elif dimension == 3:
        return (4/3) * math.pi, 4 * math.pi  # Volume and surface area of a 3-dimensional object (e.g., sphere)
    else:
        return None, None  # Calculations not defined for dimensions higher than 3