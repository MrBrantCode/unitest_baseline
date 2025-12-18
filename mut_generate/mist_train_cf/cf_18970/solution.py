"""
QUESTION:
Create a function called "calculate_hypotenuse" that takes two parameters, "side1" and "side2", representing the lengths of two sides of a right triangle, and returns the length of the third side using the Pythagorean theorem. The function should handle any positive lengths for "side1" and "side2" and should not use the math library for calculating the square root.
"""

def calculate_hypotenuse(side1, side2):
    """
    Calculate the length of the hypotenuse of a right triangle given the lengths of two sides.
    
    Args:
    side1 (float): The length of the first side.
    side2 (float): The length of the second side.
    
    Returns:
    float: The length of the hypotenuse.
    """
    side1_squared = side1 ** 2
    side2_squared = side2 ** 2
    sum_of_squares = side1_squared + side2_squared
    # Use exponentiation operator to calculate the square root without using math library
    hypotenuse = sum_of_squares ** 0.5
    return hypotenuse