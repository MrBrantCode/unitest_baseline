"""
QUESTION:
Write a Python function named `calculate_triangle_properties` that calculates and returns the area and perimeter of a triangle given three string side lengths. The function should convert the string inputs to floats, check if the sides can form a valid triangle, and round the calculated area and perimeter to two decimal places. If the sides are invalid, return an error message. The function should also handle non-numeric inputs and negative values for the sides.
"""

def calculate_triangle_properties(side1, side2, side3):
    """
    Calculate the area and perimeter of a triangle given three string side lengths.

    Args:
    side1 (str): The length of side 1.
    side2 (str): The length of side 2.
    side3 (str): The length of side 3.

    Returns:
    tuple: A tuple containing the area and perimeter of the triangle. If the sides are invalid, returns an error message.
    """
    
    # Try to convert string inputs to floats
    try:
        side1 = float(side1)
        side2 = float(side2)
        side3 = float(side3)
    except ValueError:
        return "Error: Non-numeric input"

    # Check if the given sides can form a valid triangle
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Error: Negative or zero side length"
    elif side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        # Calculate the semi-perimeter
        semiperimeter = (side1 + side2 + side3) / 2
        # Calculate the area using Heron's formula
        area = (semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)) ** 0.5
        # Calculate the perimeter
        perimeter = side1 + side2 + side3
        # Round the calculated area and perimeter to two decimal places
        return round(area, 2), round(perimeter, 2)
    else:
        return "Error: Invalid sides for a triangle"