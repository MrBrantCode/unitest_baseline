"""
QUESTION:
Write a function `calculate_triangle_properties` that takes three side lengths `side1`, `side2`, and `side3` as input and returns the area, perimeter, and a boolean value indicating whether the triangle is right-angled or not. The function should have a time complexity of O(1) and a space complexity of O(1). It should handle invalid input gracefully and return an error message if the input does not form a valid triangle. The input side lengths can be positive integers or floats.
"""

def calculate_triangle_properties(side1, side2, side3):
    """
    Calculate the properties of a triangle given three side lengths.
    
    Args:
    side1 (int or float): The length of the first side.
    side2 (int or float): The length of the second side.
    side3 (int or float): The length of the third side.
    
    Returns:
    tuple: A tuple containing the area, perimeter, and a boolean indicating whether the triangle is right-angled.
    """
    
    # Validate input
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Invalid input: Side lengths must be positive."
    
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "Invalid input: Side lengths do not form a valid triangle."
    
    # Calculate perimeter and semiperimeter
    perimeter = side1 + side2 + side3
    semiperimeter = perimeter / 2
    
    # Calculate area using Heron's formula
    area = (semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)) ** 0.5
    
    # Check if the triangle is right-angled
    is_right_angle = side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2
    
    return area, perimeter, is_right_angle