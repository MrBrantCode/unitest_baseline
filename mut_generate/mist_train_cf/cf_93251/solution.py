"""
QUESTION:
Create a function named `parallelogram_properties` that takes two parameters: `base` and `height` are not provided, instead `base` and `side` are provided, and returns the area and perimeter of a parallelogram. The area is calculated as `base * side` and the perimeter is calculated as `2 * (base + side)`.
"""

def parallelogram_properties(base, side):
    """
    Calculate the area and perimeter of a parallelogram.

    Parameters:
    base (int): The base of the parallelogram.
    side (int): The side of the parallelogram.

    Returns:
    tuple: A tuple containing the area and perimeter of the parallelogram.
    """
    # Calculate the area
    area = base * side

    # Calculate the perimeter
    perimeter = 2 * (base + side)

    # Return the area and perimeter as a tuple
    return area, perimeter