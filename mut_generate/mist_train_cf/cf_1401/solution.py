"""
QUESTION:
Create a function called `calculate_area` that takes three parameters: `side_a`, `side_b`, and `side_c`, all representing the sides of a triangle. Using only basic arithmetic operations, calculate and return the area of the triangle if it is a right triangle, where `side_c` is the hypotenuse. The function must handle invalid inputs: return an error message if `side_a`, `side_b`, or `side_c` are not integers, if `side_a` or `side_b` are negative or zero, or if the triangle is not a right triangle.
"""

def calculate_area(side_a, side_b, side_c):
    """
    Calculate the area of a right triangle given the lengths of its sides.

    Args:
        side_a (int): The length of one side of the triangle.
        side_b (int): The length of another side of the triangle.
        side_c (int): The length of the hypotenuse of the triangle.

    Returns:
        int: The area of the triangle, or an error message if the inputs are invalid.
    """
    # Check if the inputs are integers
    if not isinstance(side_a, int) or not isinstance(side_b, int) or not isinstance(side_c, int):
        return "Error: Inputs must be integers."
    
    # Check if side_a or side_b is negative or zero
    if side_a <= 0 or side_b <= 0:
        return "Error: side_a and side_b must be positive."
    
    # Check if the triangle is a right triangle
    if (side_a ** 2) + (side_b ** 2) != side_c ** 2:
        return "Error: The triangle is not a right triangle."
    
    # Calculate the area of the right triangle
    area = (side_a * side_b) / 2
    return area